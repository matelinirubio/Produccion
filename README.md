# Producción de contenido — Cáscara Foods

Repo de trabajo para el posteo orgánico de Cáscara en Facebook, Instagram y TikTok, publicado con **Buffer**.

- `marca/voz-de-marca.md`: tono, recursos y horarios para escribir copy.
- `campanas/`: planes de campañas (por ejemplo, las historias de Black Friday 2026 y cómo subirlas en tandas).
- `herramientas/variaciones_historias.py`: genera historias 1080×1920 con cuenta regresiva a partir de anuncios 4:5. Usa Poppins y Fraunces (paquetes `@fontsource` de npm, porque GitHub está bloqueado).

## Buffer
- Organización: **Cáscara Foods**. El plan permite máx. **10 posts programados a la vez por canal**, 3 canales y 1 miembro.
- Canales:

  | Canal | Estado |
  |---|---|
  | Instagram @cascarafoods (Business) | Conectado. Zona horaria America/Santiago |
  | Facebook página "Cáscara" | Conectado. Zona horaria Europe/London (pendiente cambiarla a Santiago) |
  | TikTok @cascarafoods | Conectado (reconectado el 04-11-2026) |

## Reglas aprendidas
- **Imágenes**: Buffer necesita un enlace directo y público. Se usa Drive con "cualquier persona con el enlace", en el formato `https://drive.usercontent.google.com/download?id=<ID>&export=download`. Buffer guarda el enlace, no una copia, así que el archivo debe seguir público hasta que se publique.
- **Imágenes pesadas o para TikTok**: se cargan en Archivos de Shopify con `fileCreate`, usando como origen el enlace público de Drive (Shopify las descarga por su cuenta). Después se usa el enlace del CDN con `&width=`. Desde este entorno sí se pueden subir archivos a Drive con el conector (`create_file`, pasando una referencia al archivo local en vez del contenido), pero solo de hasta unos 3 MB. Si el archivo es más grande, se sube una versión JPG más liviana (por ejemplo 2250×2813). A Shopify no se puede subir directo.
- **Instagram (publicación automática)**: solo acepta **JPG**. El CDN de Shopify entrega WebP a los servidores de Meta, así que Instagram lo rechaza con el error "issue with the media". Lo que funciona es el servicio de imágenes de Google sobre el archivo público de Drive: `https://lh3.googleusercontent.com/d/<ID>=w1440-rj` (`-rj` obliga a JPG y `w1440` fija el ancho). Probado el 04-11-2026.
- **Facebook**: acepta PNG del CDN de Shopify con `&width=1440`. Máximo 8 MB; relación de aspecto entre 4:5 y 1.91:1.
- **TikTok**: máximo 2.073.600 píxeles (1080×1920). Se usa `&width=1080` (1080×1350).
- **Videos**: el enlace directo de Drive funciona en Instagram (Reel), Facebook (video) y TikTok: `https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`. Probado el 17-11-2026 con un MP4 4:5 de 42 s y 58 MB.
- **Portada personalizada de un reel**: Buffer no la permite; solo deja elegir un fotograma del video (`thumbnailOffset`). Para usar una imagen de portada se programa en **Metricool** (`createScheduledPost` con `videoThumbnailUrl`), que tiene conectados Instagram y Facebook (TikTok no). Metricool guarda su propia copia del video y de la portada, así que no depende de que Drive siga público. Usado el 18-11-2026.
- **Historias con sticker de link (Instagram)**: no se pueden publicar solas. Van en modo aviso: llega una notificación a la app de Buffer y se publica a mano poniendo el sticker. Sin sticker sí se publican solas.
- **Historias de Facebook**: se publican solas y no llevan link.
- **Varios posts seguidos en el mismo canal**: si van separados por 1 minuto, Buffer puede publicarlos unos minutos tarde. El 18-11-2026, dos historias de Facebook programadas a las 12:01 y 12:02 salieron a las 12:08. No es un error y no hay que tocarlas; si se intenta forzar la publicación mientras Buffer las está enviando, responde 403.
- Los posts se crean en hora Chile, con offset explícito (`-03:00` en horario de verano).
- **Más de 10 posts por canal**: se suben en tandas de 10 y se deja un aviso programado en Claude para subir la tanda siguiente cuando salga la anterior. No se usa Metricool para esto.
- **Subir imágenes nuevas a Drive**: si se crean dentro de una carpeta compartida con link, heredan el permiso y `lh3` las sirve sin hacer nada más.
- **Carpetas de Drive**: la búsqueda de archivos de una carpeta viene paginada (a veces de a 5). Siempre seguir el `nextPageToken` hasta el final y confirmar cuántas láminas hay antes de programar. El 25-11-2026 el carrusel de Black Friday salió sin la lámina 6 (creatina 3x2) por no revisar la segunda página.
