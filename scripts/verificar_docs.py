"""Verifica la documentación de UniLink.

Comprobaciones:
  enlaces    todo enlace relativo de docs/ y contracts/ apunta a un archivo y un ancla que existen.
  codigos    no quedan códigos de spec antiguos fuera de la tabla de equivalencias y de docs/decisiones/.
  cobertura  cada CU-01…30 y HU-01…31 aparece exactamente una vez en docs/modulos/.
Con --fase completa, además:
  actores    cada actor de "Quién es quién" de un spec existe en la tabla de actores del SRS (§2.4).
  contratos  los JSON Schema de contracts/eventos/ y los OpenAPI de contracts/api/ son válidos.

Uso: python scripts/verificar_docs.py [--fase reorganizacion|completa]
Termina con código 0 e imprime OK si no hay problemas; si los hay, imprime uno por línea y termina con 1.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

RAIZ = Path(__file__).resolve().parent.parent
CARPETAS = [RAIZ / "docs", RAIZ / "contracts"]
TOTAL_CU = 30
TOTAL_HU = 31

CODIGO_ANTIGUO = re.compile(r"FS-(?:CTA|PRF|ADM|NOT|MSG|OPO|EVT|PRY)-\d\d")
PERMITIDOS_CODIGO_ANTIGUO = [RAIZ / "docs" / "modulos" / "README.md", RAIZ / "docs" / "decisiones"]

ENLACE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|!\[[^\]]*\]\(([^)\s]+)\)")
ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ANCLA_HTML = re.compile(r"<a\s+(?:id|name)=\"([^\"]+)\"")
BLOQUE_CODIGO = re.compile(r"^\s*(```|~~~)")


def archivos_md():
    for carpeta in CARPETAS:
        if carpeta.exists():
            yield from sorted(carpeta.rglob("*.md"))


def relativo(ruta):
    return ruta.relative_to(RAIZ).as_posix()


def lineas_fuera_de_codigo(texto):
    """Devuelve (número, línea) de las líneas que no están dentro de un bloque de código."""
    dentro = False
    for numero, linea in enumerate(texto.splitlines(), start=1):
        if BLOQUE_CODIGO.match(linea):
            dentro = not dentro
            continue
        if not dentro:
            yield numero, linea


def texto_visible(titulo):
    """Quita el formato Markdown de un encabezado como lo hace GitHub antes de crear el ancla."""
    titulo = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", titulo)
    titulo = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", titulo)
    titulo = re.sub(r"<[^>]+>", "", titulo)
    return titulo


def ancla_github(titulo):
    """Ancla que GitHub genera para un encabezado: minúsculas, sin puntuación, espacios → guiones."""
    texto = texto_visible(titulo).strip().lower()
    texto = re.sub(r"[^\w\- ]", "", texto)
    return texto.replace(" ", "-")


_anclas_cache = {}


def anclas_de(ruta):
    if ruta not in _anclas_cache:
        anclas = set()
        vistas = {}
        texto = ruta.read_text(encoding="utf-8")
        for _, linea in lineas_fuera_de_codigo(texto):
            for ancla in ANCLA_HTML.findall(linea):
                anclas.add(ancla)
            coincidencia = ENCABEZADO.match(linea)
            if coincidencia:
                base = ancla_github(coincidencia.group(2))
                repeticiones = vistas.get(base, 0)
                anclas.add(base if repeticiones == 0 else f"{base}-{repeticiones}")
                vistas[base] = repeticiones + 1
        _anclas_cache[ruta] = anclas
    return _anclas_cache[ruta]


def es_externo(destino):
    return re.match(r"^[a-z][a-z0-9+.-]*:", destino, re.IGNORECASE) is not None


def verificar_enlaces(problemas):
    for archivo in archivos_md():
        texto = archivo.read_text(encoding="utf-8")
        for numero, linea in lineas_fuera_de_codigo(texto):
            linea_sin_codigo = re.sub(r"`[^`]*`", "", linea)
            for grupo in ENLACE.findall(linea_sin_codigo):
                destino = grupo[0] or grupo[1]
                if es_externo(destino):
                    continue
                ruta_txt, _, ancla = destino.partition("#")
                ruta_txt = unquote(ruta_txt)
                ancla = unquote(ancla)
                objetivo = (archivo.parent / ruta_txt).resolve() if ruta_txt else archivo
                donde = f"{relativo(archivo)}:{numero}"
                if not objetivo.exists():
                    problemas.append(f"enlaces: {donde} → no existe '{ruta_txt}'")
                    continue
                if ancla and objetivo.is_file() and objetivo.suffix == ".md" and ancla not in anclas_de(objetivo):
                    problemas.append(f"enlaces: {donde} → no existe el ancla '#{ancla}' en '{relativo(objetivo)}'")


def permitido_codigo_antiguo(archivo):
    return any(archivo == p or p in archivo.parents for p in PERMITIDOS_CODIGO_ANTIGUO)


def verificar_codigos(problemas):
    for carpeta in CARPETAS:
        if not carpeta.exists():
            continue
        for archivo in sorted(carpeta.rglob("*")):
            if not archivo.is_file() or archivo.suffix not in {".md", ".yaml", ".yml", ".json"}:
                continue
            if permitido_codigo_antiguo(archivo):
                continue
            for numero, linea in enumerate(archivo.read_text(encoding="utf-8").splitlines(), start=1):
                for codigo in CODIGO_ANTIGUO.findall(linea):
                    problemas.append(f"codigos: {relativo(archivo)}:{numero} → código antiguo {codigo}")


def verificar_cobertura(problemas):
    modulos = RAIZ / "docs" / "modulos"
    if not modulos.exists():
        problemas.append("cobertura: no existe docs/modulos/")
        return
    for archivo_nombre, prefijo, total in (("casos-de-uso.md", "CU", TOTAL_CU), ("historias.md", "HU", TOTAL_HU)):
        apariciones = {}
        patron = re.compile(rf"^##\s+{prefijo}-(\d\d)\b")
        for archivo in sorted(modulos.glob(f"*/{archivo_nombre}")):
            for _, linea in lineas_fuera_de_codigo(archivo.read_text(encoding="utf-8")):
                coincidencia = patron.match(linea)
                if coincidencia:
                    apariciones.setdefault(int(coincidencia.group(1)), []).append(relativo(archivo))
        for n in range(1, total + 1):
            donde = apariciones.get(n, [])
            if len(donde) != 1:
                problemas.append(f"cobertura: {prefijo}-{n:02d} aparece {len(donde)} veces {donde}")
        for n in sorted(set(apariciones) - set(range(1, total + 1))):
            problemas.append(f"cobertura: {prefijo}-{n:02d} no debería existir {apariciones[n]}")


def nombres_de_tabla(texto, titulo_seccion):
    """Primera columna de la primera tabla que sigue a un encabezado que contiene titulo_seccion."""
    nombres = []
    en_seccion = False
    en_tabla = False
    for _, linea in lineas_fuera_de_codigo(texto):
        coincidencia = ENCABEZADO.match(linea)
        if coincidencia:
            if en_tabla:
                break
            en_seccion = titulo_seccion.lower() in coincidencia.group(2).lower()
            continue
        if not en_seccion:
            continue
        if linea.startswith("|"):
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if not en_tabla:
                en_tabla = True
                continue  # fila de títulos
            if set(celdas[0]) <= set("-: "):
                continue  # separador
            nombres.append(celdas[0])
        elif en_tabla:
            break
    return nombres


def normalizar_actor(nombre):
    nombre = re.sub(r"[*_`]", "", nombre)
    nombre = re.sub(r"\(.*?\)", "", nombre)
    return nombre.strip().lower()


def verificar_actores(problemas):
    srs = RAIZ / "docs" / "srs" / "Especificacion_Requisitos.md"
    if not srs.exists():
        problemas.append("actores: no existe docs/srs/Especificacion_Requisitos.md")
        return
    actores = {normalizar_actor(n) for n in nombres_de_tabla(srs.read_text(encoding="utf-8"), "Actores del sistema")}
    if not actores:
        problemas.append("actores: el SRS no tiene tabla en la sección 'Actores del sistema'")
        return
    for spec in sorted((RAIZ / "docs" / "modulos").glob("*/specs/*.md")):
        for nombre in nombres_de_tabla(spec.read_text(encoding="utf-8"), "Quién es quién"):
            if normalizar_actor(nombre) not in actores:
                problemas.append(f"actores: {relativo(spec)} → '{nombre}' no está en el SRS §2.4")


def verificar_contratos(problemas):
    try:
        import yaml
        from jsonschema import Draft202012Validator
        from openapi_spec_validator import validate
        from openapi_spec_validator.versions.shortcuts import get_spec_version
    except ImportError as error:
        problemas.append(f"contratos: falta una librería ({error.name}); instalar jsonschema y openapi-spec-validator")
        return
    eventos = RAIZ / "contracts" / "eventos"
    for archivo in sorted(eventos.glob("*.json")) if eventos.exists() else []:
        try:
            Draft202012Validator.check_schema(json.loads(archivo.read_text(encoding="utf-8")))
        except Exception as error:  # noqa: BLE001 - se informa cualquier error de lectura o validación
            problemas.append(f"contratos: {relativo(archivo)} → {str(error).splitlines()[0]}")
    api = RAIZ / "contracts" / "api"
    for archivo in sorted(api.glob("*.yaml")) if api.exists() else []:
        try:
            documento = yaml.safe_load(archivo.read_text(encoding="utf-8"))
            if documento.get("openapi") != "3.1.0":
                problemas.append(f"contratos: {relativo(archivo)} → debe declarar openapi: 3.1.0")
                continue
            get_spec_version(documento)
            validate(documento)
        except Exception as error:  # noqa: BLE001
            problemas.append(f"contratos: {relativo(archivo)} → {str(error).splitlines()[0]}")


def main():
    parser = argparse.ArgumentParser(description="Verifica la documentación de UniLink.")
    parser.add_argument("--fase", choices=["reorganizacion", "completa"], default="reorganizacion")
    argumentos = parser.parse_args()

    problemas = []
    verificar_enlaces(problemas)
    verificar_codigos(problemas)
    verificar_cobertura(problemas)
    if argumentos.fase == "completa":
        verificar_actores(problemas)
        verificar_contratos(problemas)

    if problemas:
        print("\n".join(problemas))
        print(f"\n{len(problemas)} problema(s).")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
