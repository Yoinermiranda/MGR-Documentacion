# Plantilla base (_template)

Esta carpeta contiene la **base** desde donde se genera el menú principal
de todas las páginas del sitio.

## Archivos

- **header.html** — La cabecera/menú principal (marca + enlaces a
  Manual de Usuario, Manual Técnico e Informe Final). Edita este archivo
  para cambiar textos, enlaces o agregar/quitar elementos del menú principal.

- **build_site.py** — Script que genera la portada (`index.html`) y las
  16 páginas de `secciones/` a partir de:
  - el contenido de `header.html` (menú principal),
  - la lista de capítulos definida dentro del propio script (sidebar,
    títulos, descripciones y checklist de cada sección).

## ¿Cómo aplico un cambio en el menú principal?

1. Edita `header.html` (por ejemplo, cambia la URL del Manual de Usuario
   o el texto de un enlace). El marcador `{{PREFIX}}` no se debe borrar:
   el script lo reemplaza automáticamente por la ruta correcta según el
   nivel de cada página.
2. Desde la carpeta `MGR-Documentacion/`, ejecuta:

   ```bash
   python3 _template/build_site.py
   ```

3. Listo: la portada y las 16 secciones quedan regeneradas con el nuevo
   menú principal, conservando el resto del contenido de cada página
   (porque ese contenido también se vuelve a generar desde el script;
   si ya editaste el contenido de alguna sección a mano, haz una copia
   de seguridad antes de volver a correr el script).

## ¿Y si quiero editar el contenido de cada capítulo directamente en el HTML?

Puedes hacerlo sin problema: edita `secciones/XX-nombre/index.html`
directamente. Solo ten en cuenta que si vuelves a correr `build_site.py`,
esos cambios de contenido se sobrescriben (el script solo conserva lo que
está definido en sí mismo). Si vas a editar el contenido a mano de forma
permanente, lo más seguro es no volver a correr el script — o pedirle a
Claude que aplique los cambios de menú directamente sobre los 17 archivos
ya editados.
