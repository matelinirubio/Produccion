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
| 2 | 11–20 | sáb 28, 20:15 → lun 30, 8:31 | sáb 28, 16:45 |
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
