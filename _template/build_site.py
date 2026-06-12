import os

ROOT = "/home/claude/MGR-Documentacion"
SECCIONES = os.path.join(ROOT, "secciones")

# ----------------------------------------------------------------
# Definición de capítulos: (num, slug, titulo, grupo, intro, items)
# ----------------------------------------------------------------
GROUPS = [
    ("Fundamentos del proyecto", [
        ("01", "introduccion", "Introducción",
         "Presenta el documento al lector: de qué trata el proyecto, en qué contexto se desarrolla y cómo está organizado el resto de la documentación.",
         [
             "Contexto general del proyecto y la entidad o problemática para la que se desarrolla.",
             "Resumen muy breve del problema que motiva el desarrollo (se detalla más adelante).",
             "Explicación de cómo está estructurado este documento y cómo navegar entre secciones.",
         ]),
        ("02", "resumen-proyecto", "Resumen del Proyecto",
         "Una síntesis ejecutiva del proyecto completo: qué se construyó, para quién y qué problema resuelve, pensada para que cualquier lector entienda el panorama en pocos párrafos.",
         [
             "Descripción general del producto o sistema desarrollado.",
             "Público objetivo / usuarios finales.",
             "Objetivo general expresado en una sola frase.",
             "Resultado o entregable final esperado.",
         ]),
        ("03", "planteamiento", "Formulación del Problema",
         "Describe la situación actual que origina el proyecto, sus causas y consecuencias, y formula la pregunta o problema central que el proyecto busca resolver.",
         [
             "Descripción de la situación actual (problemática).",
             "Causas que generan el problema.",
             "Efectos o consecuencias si el problema no se resuelve.",
             "Pregunta de investigación o problema central, claramente formulado.",
         ]),
        ("04", "objetivos", "Objetivos",
         "Define el objetivo general del proyecto y los objetivos específicos que, en conjunto, permiten alcanzarlo.",
         [
             "Objetivo general: qué se quiere lograr con el proyecto en su totalidad.",
             "Objetivos específicos: pasos concretos y medibles para alcanzar el objetivo general.",
             "Verificar que cada objetivo específico use un verbo en infinitivo (analizar, diseñar, implementar, evaluar...).",
         ]),
    ]),
    ("Marco y alcance", [
        ("05", "alcance-justificacion", "Alcance y Justificación",
         "Delimita qué incluye y qué no incluye el proyecto, y argumenta por qué es importante, viable y pertinente desarrollarlo.",
         [
             "Alcance: funcionalidades, módulos o procesos que cubre el proyecto.",
             "Delimitaciones: lo que queda fuera del alcance (tiempo, población, tecnología, etc.).",
             "Justificación: pertinencia, viabilidad e impacto esperado del proyecto.",
             "Beneficiarios directos e indirectos.",
         ]),
        ("06", "marcos", "Marcos (Conceptual, Legal y Teórico)",
         "Reúne los fundamentos que sustentan el proyecto desde tres ángulos: los conceptos clave, las teorías o modelos en los que se apoya y las normas legales o institucionales que aplican.",
         [
             "Marco conceptual: definición de términos clave usados a lo largo del documento.",
             "Marco teórico: teorías, modelos o enfoques que fundamentan las decisiones del proyecto.",
             "Marco legal: leyes, normas, reglamentos o políticas institucionales aplicables (ej. protección de datos, normas técnicas).",
         ]),
        ("07", "marco-tecnologico", "Marco Tecnológico",
         "Documenta las tecnologías, lenguajes, herramientas y la infraestructura utilizada para desarrollar el sistema.",
         [
             "Lenguajes de programación y frameworks utilizados (frontend y backend).",
             "Bases de datos y motores de almacenamiento.",
             "Herramientas de desarrollo: editores, control de versiones, gestión de proyectos.",
             "Infraestructura de despliegue: servidores, hosting, servicios en la nube.",
         ]),
    ]),
    ("Desarrollo del proyecto", [
        ("08", "metodologia-scrum", "Metodología Scrum",
         "Explica cómo se aplicó la metodología Scrum durante el desarrollo: roles del equipo, artefactos generados y eventos realizados durante los sprints.",
         [
             "Roles del equipo: Product Owner, Scrum Master, equipo de desarrollo.",
             "Artefactos: Product Backlog, Sprint Backlog, incrementos del producto.",
             "Eventos: Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective.",
             "Cronograma o calendario de los sprints ejecutados.",
         ]),
        ("09", "historias-usuario", "Historias de Usuario",
         "Presenta las historias de usuario que describen las necesidades del usuario en formato ágil, junto con sus criterios de aceptación.",
         [
             "Formato sugerido: \"Como [rol], quiero [funcionalidad], para [beneficio]\".",
             "Tabla con: identificador, historia, criterios de aceptación, prioridad y estimación (puntos de historia).",
             "Relación de cada historia con los objetivos específicos del proyecto.",
         ]),
        ("10", "requerimientos-funcionales", "Requerimientos Funcionales",
         "Lista las funciones específicas que el sistema debe ser capaz de realizar.",
         [
             "Tabla de requerimientos: código (RF-01, RF-02...), nombre, descripción, prioridad.",
             "Relación de cada requerimiento con la(s) historia(s) de usuario que lo originan.",
         ]),
        ("11", "requerimientos-no-funcionales", "Requerimientos No Funcionales",
         "Describe las cualidades y restricciones que debe cumplir el sistema, más allá de sus funciones específicas.",
         [
             "Categorías típicas: rendimiento, seguridad, usabilidad, disponibilidad, escalabilidad, mantenibilidad.",
             "Tabla de requerimientos: código (RNF-01, RNF-02...), categoría, descripción, criterio de cumplimiento.",
         ]),
        ("12", "diagramas-sistema", "Diagramas del Sistema",
         "Incluye los diagramas que representan visualmente la estructura, el comportamiento y los flujos del sistema.",
         [
             "Diagrama de casos de uso.",
             "Diagrama de arquitectura del sistema.",
             "Diagramas de flujo o de secuencia de los procesos principales.",
             "Cualquier otro diagrama UML relevante (clases, componentes, despliegue).",
         ]),
        ("13", "modelo-relacional", "Modelo Relacional",
         "Documenta la estructura de la base de datos: entidades, relaciones, atributos y el diccionario de datos correspondiente.",
         [
             "Diagrama entidad-relación (ERD) del sistema.",
             "Diccionario de datos: tablas, campos, tipos de dato, llaves primarias y foráneas.",
             "Reglas de negocio relevantes a nivel de datos (restricciones, integridad referencial).",
         ]),
        ("14", "prototipo-interfaz", "Prototipo e Interfaz",
         "Presenta los wireframes, mockups o capturas del prototipo desarrollado, junto con la justificación de las decisiones de diseño.",
         [
             "Wireframes o mockups de las pantallas principales.",
             "Capturas de pantalla del prototipo funcional (si existe).",
             "Justificación de las decisiones de experiencia de usuario (UX) e interfaz (UI).",
         ]),
    ]),
    ("Cierre", [
        ("15", "conclusiones", "Conclusiones",
         "Recoge las conclusiones generales del proyecto, evalúa el cumplimiento de los objetivos planteados y propone recomendaciones o trabajo futuro.",
         [
             "Conclusiones generales del proyecto.",
             "Cumplimiento de cada objetivo específico planteado en la sección 04.",
             "Lecciones aprendidas durante el desarrollo.",
             "Recomendaciones y posibles líneas de trabajo futuro.",
         ]),
        ("16", "referencias", "Bibliografía",
         "Lista todas las fuentes consultadas y citadas a lo largo del documento, siguiendo el formato de citación definido (APA u otro).",
         [
             "Listado de referencias en orden alfabético, siguiendo normas APA (u otra norma definida por la institución).",
             "Incluir libros, artículos, documentación oficial de tecnologías y recursos web utilizados.",
         ]),
    ]),
]

# Lista plana de capítulos en orden
CHAPTERS = []
for group_name, items in GROUPS:
    for num, slug, title, intro, checklist in items:
        CHAPTERS.append({
            "num": num,
            "slug": slug,
            "title": title,
            "group": group_name,
            "intro": intro,
            "checklist": checklist,
        })

FONT_LINKS = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">"""

# ----------------------------------------------------------------
# Cabecera principal del sitio (menú principal): se define en
# _template/header.html para que sea fácil de editar sin tocar
# este script. Se reemplaza {{PREFIX}} con '' (portada) o '../../'
# (secciones) para que las rutas funcionen en cada nivel.
# ----------------------------------------------------------------
TEMPLATE_DIR = os.path.join(ROOT, "_template")


def build_site_header(prefix):
    """Carga _template/header.html y ajusta las rutas según el prefijo
    ('' para la portada, '../../' para cada sección)."""
    with open(os.path.join(TEMPLATE_DIR, "header.html"), encoding="utf-8") as f:
        raw = f.read()

    # Quitar el bloque de comentario explicativo (<!-- ... -->) antes de insertar
    if raw.lstrip().startswith("<!--"):
        end = raw.find("-->")
        raw = raw[end + 3:]

    html = raw.replace("{{PREFIX}}", prefix).strip()
    # Re-indentar para que quede alineado dentro de <body>
    return "\n".join("  " + line if line else line for line in html.splitlines())



def build_sidebar(current_num, css_prefix):
    """Construye el HTML del sidebar de navegación por capítulos."""
    parts = []
    parts.append(f'    <a class="sidebar-home" href="{css_prefix}index.html">&larr; Portada</a>')
    parts.append('    <span class="sidebar-tagline">Capítulos del documento</span>')

    for group_name, items in GROUPS:
        parts.append('    <div class="sidebar-group">')
        parts.append(f'      <p class="sidebar-group-title">{group_name}</p>')
        parts.append('      <nav><ul>')
        for num, slug, title, *_ in items:
            active = ' active' if num == current_num else ''
            href = f"{css_prefix}secciones/{num}-{slug}/index.html"
            parts.append(
                f'        <li><a class="{active.strip()}" href="{href}">'
                f'<span class="num">{num}</span><span>{title}</span></a></li>'.replace('class="" ', '')
                if not active else
                f'        <li><a class="active" href="{href}">'
                f'<span class="num">{num}</span><span>{title}</span></a></li>'
            )
        parts.append('      </ul></nav>')
        parts.append('    </div>')
    return "\n".join(parts)


def build_section_page(chapter, index_in_list):
    num = chapter["num"]
    slug = chapter["slug"]
    title = chapter["title"]
    intro = chapter["intro"]
    checklist = chapter["checklist"]

    # Página anterior / siguiente
    prev_chapter = CHAPTERS[index_in_list - 1] if index_in_list > 0 else None
    next_chapter = CHAPTERS[index_in_list + 1] if index_in_list < len(CHAPTERS) - 1 else None

    if prev_chapter:
        prev_html = (
            f'      <a class="prev" href="../{prev_chapter["num"]}-{prev_chapter["slug"]}/index.html">'
            f'<span class="nav-label">&larr; Anterior</span>'
            f'<span class="nav-title">{prev_chapter["num"]}. {prev_chapter["title"]}</span></a>'
        )
    else:
        prev_html = (
            '      <a class="prev" href="../../index.html">'
            '<span class="nav-label">&larr; Anterior</span>'
            '<span class="nav-title">Portada</span></a>'
        )

    if next_chapter:
        next_html = (
            f'      <a class="next" href="../{next_chapter["num"]}-{next_chapter["slug"]}/index.html">'
            f'<span class="nav-label">Siguiente &rarr;</span>'
            f'<span class="nav-title">{next_chapter["num"]}. {next_chapter["title"]}</span></a>'
        )
    else:
        next_html = '      <a class="next placeholder" href="#" aria-hidden="true"><span class="nav-label">&nbsp;</span><span class="nav-title">&nbsp;</span></a>'

    checklist_html = "\n".join(f"            <li>{item}</li>" for item in checklist)

    sidebar_html = build_sidebar(num, "../../")

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{num}. {title} — Documentación MGR</title>
{FONT_LINKS}
  <link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
{build_site_header("../../")}
  <div class="layout">
    <aside class="sidebar">
{sidebar_html}
    </aside>

    <main class="content">
      <div class="content-inner">
        <header class="content-header">
          <span class="eyebrow">Capítulo {num} · {chapter["group"]}</span>
          <h1>{title}</h1>
          <p class="subtitle">{intro}</p>
        </header>

        <article class="prose">
          <div class="guide-box">
            <span class="guide-label">Contenido sugerido para esta sección</span>
            <ul>
{checklist_html}
            </ul>
          </div>

          <p>
            Reemplaza este texto guía por el contenido real de <strong>{title.lower()}</strong>.
            Puedes usar encabezados (<code>&lt;h2&gt;</code>, <code>&lt;h3&gt;</code>), párrafos, listas,
            tablas e imágenes según lo necesite cada apartado.
          </p>
        </article>

        <footer class="page-nav">
{prev_html}
{next_html}
        </footer>
      </div>
    </main>
  </div>
</body>
</html>
"""


def build_cover_page():
    sidebar_html = build_sidebar(None, "")

    toc_groups_html = []
    for group_name, items in GROUPS:
        cards = []
        for num, slug, title, *_ in items:
            cards.append(
                f'        <a class="toc-card" href="secciones/{num}-{slug}/index.html">'
                f'<span class="toc-num">{num}</span><span class="toc-title">{title}</span></a>'
            )
        cards_html = "\n".join(cards)
        toc_groups_html.append(
            f'      <div class="toc-group">\n'
            f'        <h3 class="toc-group-title">{group_name}</h3>\n'
            f'        <div class="toc-grid">\n{cards_html}\n        </div>\n'
            f'      </div>'
        )
    toc_html = "\n".join(toc_groups_html)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Documentación MGR</title>
{FONT_LINKS}
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
{build_site_header("")}
  <div class="layout">
    <aside class="sidebar">
{sidebar_html}
    </aside>

    <main class="content" style="padding:0;">
      <div class="content-inner" style="max-width:none; width:100%;">

        <section class="cover">
          <div class="cover-content">
            <p class="cover-eyebrow">Documentación técnica de proyecto</p>
            <h1>Proyecto <em>MGR</em><br>Documentación técnica</h1>
            <p class="lead">
              Este documento reúne, capítulo por capítulo, el sustento, el desarrollo y los
              resultados del proyecto: desde la formulación del problema hasta el modelo de
              datos, el prototipo y las conclusiones finales.
            </p>

            <dl class="cover-meta">
              <div>
                <dt>Autor(es)</dt>
                <dd>[Nombre de los integrantes]</dd>
              </div>
              <div>
                <dt>Programa / Institución</dt>
                <dd>[Nombre del programa académico]</dd>
              </div>
              <div>
                <dt>Versión</dt>
                <dd>[Fecha / versión del documento]</dd>
              </div>
            </dl>

            <p class="cover-scroll">Tabla de contenidos</p>
          </div>
        </section>

        <section class="toc">
          <h2 class="toc-heading">Contenido del documento</h2>
          <p class="toc-sub">
            16 capítulos organizados en cuatro bloques: fundamentos del proyecto, marco y
            alcance, desarrollo del proyecto y cierre.
          </p>

{toc_html}
        </section>

      </div>
    </main>
  </div>
</body>
</html>
"""


def main():
    # Página principal
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_cover_page())

    # Páginas de cada sección
    for i, chapter in enumerate(CHAPTERS):
        folder = os.path.join(SECCIONES, f'{chapter["num"]}-{chapter["slug"]}')
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(build_section_page(chapter, i))

    print(f"Generadas {len(CHAPTERS)} secciones + portada.")


if __name__ == "__main__":
    main()
