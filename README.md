# Producción de contenido — Cáscara Foods

Repo de trabajo para el posteo orgánico de Cáscara en Facebook, Instagram y TikTok, publicado con **Buffer**.

- `marca/voz-de-marca.md`: tono, recursos y horarios para escribir copy.

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
- **Imágenes pesadas o para TikTok**: se cargan en Archivos de Shopify con `fileCreate`, usando como origen el enlace público de Drive (Shopify las descarga por su cuenta). Después se usa el enlace del CDN con `&width=`. Desde este entorno no se pueden subir archivos binarios ni a Drive ni a Shopify.
- **Instagram (publicación automática)**: solo acepta **JPG**. El CDN de Shopify entrega WebP a los servidores de Meta, así que Instagram lo rechaza con el error "issue with the media". Lo que funciona es el servicio de imágenes de Google sobre el archivo público de Drive: `https://lh3.googleusercontent.com/d/<ID>=w1440-rj` (`-rj` obliga a JPG y `w1440` fija el ancho). Probado el 04-11-2026.
- **Facebook**: acepta PNG del CDN de Shopify con `&width=1440`. Máximo 8 MB; relación de aspecto entre 4:5 y 1.91:1.
- **TikTok**: máximo 2.073.600 píxeles (1080×1920). Se usa `&width=1080` (1080×1350).
- **Videos**: el enlace directo de Drive funciona en Instagram (Reel), Facebook (video) y TikTok: `https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`. Probado el 17-11-2026 con un MP4 4:5 de 42 s y 58 MB.
- **Historias con sticker de link (Instagram)**: no se pueden publicar solas. Van en modo aviso: llega una notificación a la app de Buffer y se publica a mano poniendo el sticker. Sin sticker sí se publican solas.
- **Historias de Facebook**: se publican solas y no llevan link.
- Los posts se crean en hora Chile, con offset explícito (`-03:00` en horario de verano).
