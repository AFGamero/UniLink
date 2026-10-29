"""Genera el diagrama UML de casos de uso del MVP de UniLink en SVG.

Uso: python scripts/diagrama_casos_de_uso.py
Escribe docs/diagramas/casos-de-uso-mvp.svg. Si cambian los casos de uso del MVP
(docs/actores_y_alcance_mvp.md, sección 4.2), actualizar este script y volver a ejecutarlo.
"""
from pathlib import Path
from xml.sax.saxutils import escape

salida = Path(__file__).resolve().parent.parent / "docs" / "diagramas" / "casos-de-uso-mvp.svg"
W, H = 1420, 1040
partes = []


def add(s):
    partes.append(s)


TINTA = "#1f2937"
LINEA = "#374151"
SUAVE = "#6b7280"
PAQ_FONDO = "#f3f4f6"
PAQ_BORDE = "#9ca3af"
OVALO = "#ffffff"
OVALO_BORDE = "#1f2937"
NUEVO = "#fef3c7"
NUEVO_BORDE = "#b45309"

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="Segoe UI, Helvetica, Arial, sans-serif" role="img" '
    f'aria-label="Diagrama de casos de uso del MVP de UniLink">')
add('<defs><marker id="gen" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="14" markerHeight="14" orient="auto">'
    f'<path d="M0,0 L12,6 L0,12 Z" fill="#ffffff" stroke="{LINEA}" stroke-width="1.2"/></marker></defs>')
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
add(f'<text x="{W/2}" y="34" text-anchor="middle" font-size="22" font-weight="700" fill="{TINTA}">'
    'UniLink — Diagrama de casos de uso del MVP</text>')
add(f'<text x="{W/2}" y="58" text-anchor="middle" font-size="13" fill="{SUAVE}">'
    'Monitorías académicas · Semilleros de investigación · Ayudantías académicas · Actividades complementarias</text>')

# Límite del sistema
BX0, BY0, BX1, BY1 = 360, 68, 1170, 1010
add(f'<rect x="{BX0}" y="{BY0}" width="{BX1-BX0}" height="{BY1-BY0}" fill="none" stroke="{TINTA}" stroke-width="2" rx="6"/>')
add(f'<text x="{BX0+14}" y="{BY0+24}" font-size="15" font-weight="700" fill="{TINTA}">«sistema» UniLink — MVP</text>')

centros = {}


def paquete(x0, y0, x1, y1, titulo):
    add(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="{PAQ_FONDO}" stroke="{PAQ_BORDE}" '
        f'stroke-dasharray="5 4" rx="6"/>')
    add(f'<text x="{x0+10}" y="{y0+18}" font-size="12" font-weight="700" fill="{SUAVE}">{escape(titulo)}</text>')


def ovalo(cx, cy, codigo, nombre, rx=168, nuevo=False):
    fondo, borde = (NUEVO, NUEVO_BORDE) if nuevo else (OVALO, OVALO_BORDE)
    add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="23" fill="{fondo}" stroke="{borde}" stroke-width="1.5"/>')
    etiqueta = codigo + ("  (nuevo)" if nuevo else "")
    add(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="12" font-weight="700" fill="{TINTA}">{escape(etiqueta)}</text>')
    add(f'<text x="{cx}" y="{cy+12}" text-anchor="middle" font-size="12" fill="{TINTA}">{escape(nombre)}</text>')
    centros[codigo] = (cx, cy, rx)


# Columna A: base y líneas de oferta
AX, AX0, AX1 = 580, 390, 770
paquete(AX0, 100, AX1, 440, "Base: cuenta, perfil y notificaciones")
for i, (c, n) in enumerate([
    ("CU-01", "Activar cuenta precreada"),
    ("CU-02", "Iniciar sesión"),
    ("CU-17", "Recuperar contraseña"),
    ("CU-03", "Administrar mi cuenta"),
    ("CU-04", "Editar mi perfil"),
    ("CU-23", "Consultar notificaciones"),
]):
    ovalo(AX, 148 + i * 52, c, n)

paquete(AX0, 458, AX1, 590, "Monitorías académicas")
ovalo(AX, 504, "CU-31", "Obtener la condición de monitor académico", nuevo=True)
ovalo(AX, 556, "CU-05", "Buscar monitores y contactarlos")

paquete(AX0, 608, AX1, 690, "Semilleros de investigación")
ovalo(AX, 654, "CU-11", "Gestionar semillero y solicitar ingreso")

paquete(AX0, 708, AX1, 790, "Ayudantías académicas")
ovalo(AX, 754, "CU-12", "Consultar convocatorias de ayudantía")

paquete(AX0, 808, AX1, 990, "Actividades complementarias")
ovalo(AX, 854, "CU-20", "Publicar actividad complementaria")
ovalo(AX, 906, "CU-21", "Explorar actividades complementarias")
ovalo(AX, 958, "CU-15", "Inscribirse a una actividad")

# Columna B: administración y leyenda
BXc, BXa, BXb = 985, 820, 1150
paquete(BXa, 100, BXb, 300, "Administración")
ovalo(BXc, 148, "CU-24", "Administrar cuentas", rx=150)
ovalo(BXc, 200, "CU-25", "Retirar semillero o actividad", rx=150)
ovalo(BXc, 252, "CU-26", "Administrar catálogos", rx=150)


def borde_izq(c):
    x, y, rx = centros[c]
    return x - rx, y


def borde_der(c):
    x, y, rx = centros[c]
    return x + rx, y


def linea(x1, y1, x2, y2, extra=""):
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{LINEA}" stroke-width="1.3" {extra}/>')


def actor(x, y, nombre, abstracto=False):
    """Monigote con la cabeza en y-34 y los pies en y+34; devuelve el punto de anclaje (hombros)."""
    add(f'<g stroke="{TINTA}" stroke-width="2" fill="none">'
        f'<circle cx="{x}" cy="{y-26}" r="9" fill="#ffffff"/>'
        f'<line x1="{x}" y1="{y-17}" x2="{x}" y2="{y+8}"/>'
        f'<line x1="{x-16}" y1="{y-8}" x2="{x+16}" y2="{y-8}"/>'
        f'<line x1="{x}" y1="{y+8}" x2="{x-12}" y2="{y+28}"/>'
        f'<line x1="{x}" y1="{y+8}" x2="{x+12}" y2="{y+28}"/></g>')
    estilo = ' font-style="italic"' if abstracto else ""
    for i, parte in enumerate(nombre.split("\n")):
        add(f'<text x="{x}" y="{y+46+i*15}" text-anchor="middle" font-size="13" font-weight="600"{estilo} '
            f'fill="{TINTA}">{escape(parte)}</text>')


def sistema(x, y, nombre):
    lineas = nombre.split("\n")
    alto = 30 + 15 * len(lineas)
    add(f'<rect x="{x-100}" y="{y-alto/2}" width="200" height="{alto}" fill="#ffffff" stroke="{TINTA}" stroke-width="1.5" rx="4"/>')
    add(f'<text x="{x}" y="{y-alto/2+18}" text-anchor="middle" font-size="11" fill="{SUAVE}">«sistema externo»</text>')
    for i, parte in enumerate(lineas):
        add(f'<text x="{x}" y="{y-alto/2+35+i*15}" text-anchor="middle" font-size="12" font-weight="600" '
            f'fill="{TINTA}">{escape(parte)}</text>')
    return x - 100


# Actores de la izquierda
actor(150, 190, "Visitante")
for c in ("CU-01", "CU-02", "CU-17"):
    linea(168, 182, *borde_izq(c))

actor(150, 360, "Miembro de la\ncomunidad", abstracto=True)
for c in ("CU-03", "CU-04", "CU-23"):
    linea(168, 352, *borde_izq(c))

actor(270, 480, "Profesor")
for c in ("CU-05", "CU-11"):
    linea(288, 472, *borde_izq(c))

actor(90, 610, "Estudiante")
for c in ("CU-31", "CU-05", "CU-11", "CU-12", "CU-21", "CU-15"):
    linea(108, 602, *borde_izq(c))

actor(90, 780, "Monitor\nacadémico")
actor(270, 900, "Personal de\nBienestar")
linea(288, 892, *borde_izq("CU-20"))

# Generalizaciones: Monitor → Estudiante; Estudiante, Profesor y Bienestar → Miembro de la comunidad
linea(90, 744, 90, 676, 'marker-end="url(#gen)"')
TRONCO = 30
linea(72, 600, TRONCO, 600)
linea(250, 480, 214, 480)
linea(214, 480, 214, 444)
linea(214, 444, TRONCO, 444)
linea(250, 900, 214, 900)
linea(214, 900, 214, 990)
linea(214, 990, TRONCO, 990)
linea(TRONCO, 990, TRONCO, 360)
linea(TRONCO, 360, 128, 360, 'marker-end="url(#gen)"')

# Actores de la derecha
actor(1290, 200, "Administrador\nde la plataforma")
for c in ("CU-24", "CU-25", "CU-26"):
    linea(1272, 192, *borde_der(c))

xs = sistema(1290, 504, "API Vicerrectoría\nAcadémica")
linea(xs, 504, *borde_der("CU-31"))
xs = sistema(1290, 754, "API Vicerrectoría de\nExtensión y Proyección Social")
linea(xs, 754, *borde_der("CU-12"))

# Leyenda
LX, LY = BXa, 812
add(f'<rect x="{LX}" y="{LY}" width="{BXb-LX}" height="178" fill="#ffffff" stroke="{PAQ_BORDE}" rx="6"/>')
add(f'<text x="{LX+12}" y="{LY+20}" font-size="12" font-weight="700" fill="{TINTA}">Cómo leerlo</text>')
leyenda = [
    "Línea continua: el actor participa en el caso de uso.",
    "Flecha con triángulo: generalización (hereda los",
    "casos de uso del actor al que apunta).",
    "Miembro de la comunidad (cursiva) es abstracto: agrupa",
    "lo común a Estudiante, Profesor y Personal de Bienestar.",
    "El Monitor es un Estudiante: solo agrega datos extra",
    "a su perfil (CU-04); sus datos oficiales llegan por CU-31.",
    "Ayudantías y monitorías se postulan fuera de UniLink.",
]
for i, t in enumerate(leyenda):
    add(f'<text x="{LX+12}" y="{LY+40+i*17}" font-size="11" fill="{SUAVE}">{escape(t)}</text>')

add(f'<text x="{W-20}" y="{H-10}" text-anchor="end" font-size="10" fill="{SUAVE}">'
    'Fuente: docs/actores_y_alcance_mvp.md §4.2 · 2026-10-29</text>')
add("</svg>")
open(salida, "w", encoding="utf-8").write("\n".join(partes))
print(salida)
