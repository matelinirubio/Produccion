# Black Friday 2026 · historias

Black Friday del miércoles 25-11 al miércoles 2-12-2026. Son 38 historias para Instagram y Facebook, publicadas con Buffer. Se publican solas y no llevan sticker de link.

- `historias.json`: el plan completo. Cada historia tiene su número, la hora (`dueAt`, en hora de Chile), la pieza, el tipo (imagen o video) y la URL pública que se le pasa a Buffer.
- Imágenes: `lh3.googleusercontent.com/d/<ID>=w1080-rj`, en JPG de 1080×1920.
- Videos: `drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`.
- Las variaciones V1 a V8 (cuenta regresiva con un anuncio dentro) están en Drive, en `Historias/H_BLACK_FRIDAY/H_BF_variaciones`.

## Tandas en Buffer
El plan de Buffer permite máximo 10 posts programados por canal, así que las historias se suben de a 10 por canal.

| Tanda | Historias | Desde → hasta | Cuándo se sube |
|---|---|---|---|
| 1 | 1–10 | vie 27, 9:15 → sáb 28, 16:31 | jue 26 en la noche (hecho) |
| 2 | 11–20 | sáb 28, 20:15 → lun 30, 8:31 | sáb 28, 18:00 (antes 16:45; se movió por las historias de Chocolate Naranja) |
| 3 | 21–30 | lun 30, 12:45 → mar 1, 20:46 | lun 30, 8:45 |
| 4 | 31–38 | mié 2, 8:00 → mié 2, 21:31 | mar 1, 21:00 |

Hay un aviso programado en Claude para cada tanda y otro el miércoles 2 a las 21:50 para revisar que todo haya salido.

## Cómo subir una tanda
1. Listar en Buffer los posts `scheduled` y `sending` de cada canal (organización `5c3ce57875bcc1472d376408`). Hay que contar cuántos cupos libres quedan por canal (10 menos los programados).
2. Revisar también los posts `sent` y `error` de la tanda anterior. Si alguno tiene error, avisar al usuario.
3. Tomar del plan las historias siguientes que todavía no estén en Buffer (se comparan por `dueAt` y canal) y cuya hora todavía no haya pasado. Si una hora ya pasó, no se publica tarde: se salta y se avisa.
4. Crearlas en orden en los dos canales:
   - Instagram `5c3ce81e93235d7d7e63ad22`: `metadata.instagram = {type: "story", shouldShareToFeed: false}`.
   - Facebook `5c3ce84393235d7d9326fdba`: `metadata.facebook = {type: "story"}`.
   - Para ambos: `schedulingType: automatic`, `mode: customScheduled`, `dueAt` del plan, sin texto. Las imágenes llevan `altText`.
5. Si algo no cabe porque no hay cupo, dejarlo para la tanda siguiente y avisar.

## Reel de inicio (viernes 27-11, 10:00)
- Video: AD_NOV_101 vertical con dos cambios. La caja "7 sabores…" ahora dice "¡Empezó el Black Friday! hasta 45% OFF", y al cierre se agregó "Solo hasta el miércoles 2/12". Está en Drive, en la carpeta `reels` (`REEL_inicio_black_friday.mp4`, id `1W2Abl9bOXtRAlUpYE1Vwa-UkAsUMOq_X`).
- Copy A. En Facebook va con link directo a cascarafoods.cl.
- TikTok quedó programado el jueves en la noche. Instagram y Facebook los programa un aviso a las 9:20 del viernes, cuando se liberan cupos.

## Volvió el stock: Chocolate Naranja (viernes 27 y sábado 28)
- Creativos del equipo (Drive `18DhURY-MnqKhJvwUvEELmbtyvD5s1PlX`): H_AD_NOV_choconaranja_1 a 4, en formato historia.
- Instagram y Facebook en historia: 1 y 2 el viernes 27 a las 18:30 y 18:31, 3 y 4 el sábado 28 a las 17:45 y 17:46.
- TikTok: Buffer no publica historias en TikTok, así que va un post de fotos con dos láminas. Las láminas 1 y 2 salen el viernes a las 18:30 con el copy "Sí, VOLVIÓ…", y la 3 y la 4 el sábado a las 17:45 con el copy "¿Team chocolate o team naranja?…".
- Estas historias usan cupos de Buffer, por eso la tanda 2 de Black Friday se sube a las 18:00 del sábado, cuando ya salieron.
