"""Genera historias 1080x1920 de Black Friday con cuenta regresiva a partir de anuncios 4:5."""
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE = Path(sys.argv[1])  # carpeta bfstories
OUT = BASE / "variaciones"
OUT.mkdir(exist_ok=True)
F = BASE / "fonts2"
POP = {w: str(F / f"fontsource-poppins/package/files/poppins-latin-{w}-normal.woff") for w in (600, 700, 800, 900)}
FRA = {w: str(F / f"fontsource-fraunces/package/files/fraunces-latin-{w}-normal.woff") for w in (800, 900)}

W, H = 1080, 1920

PALETTES = {
    # bg_top, bg_bottom, headline, sub, pill_bg, pill_text
    "verde": ((0, 112, 88), (0, 96, 74), (205, 253, 177), (255, 255, 255), (205, 253, 177), (0, 90, 70)),
    "lima": ((140, 238, 91), (210, 255, 186), (0, 90, 70), (0, 90, 70), (0, 96, 74), (205, 253, 177)),
    "lila": ((233, 188, 255), (189, 160, 240), (70, 28, 120), (70, 28, 120), (70, 28, 120), (255, 255, 255)),
    "azul": ((38, 133, 197), (150, 205, 240), (255, 255, 255), (255, 255, 255), (12, 60, 110), (255, 255, 255)),
    "coral": ((235, 101, 110), (246, 190, 175), (255, 255, 255), (255, 255, 255), (140, 28, 45), (255, 255, 255)),
}

VARIANTS = [
    # nombre, paleta, linea1 (sans), linea2 (serif grande), bajada, anuncio
    ("V1_el_black_sigue", "verde", "EL BLACK", "SIGUE", "Hasta 45% OFF y regalos hasta el miércoles 2/12", "AD_NOV_62"),
    ("V2_finde_black", "coral", "FINDE", "BLACK", "Hasta 45% OFF en toooodos los productos", "AD_NOV_71"),
    ("V3_ya_elegiste", "lima", "¿YA ELEGISTE", "TU PACK?", "Prote, creatina, Azana o colágeno: hay descuento para todo", "AD_NOV_88"),
    ("V4_quedan_3_dias", "azul", "QUEDAN", "3 DÍAS", "El Black Friday termina el miércoles 2/12", "AD_NOV_86"),
    ("V5_quedan_2_dias", "lila", "QUEDAN", "2 DÍAS", "Hasta 45% OFF y regalos, solo hasta el miércoles", "AD_NOV_63"),
    ("V6_manana_termina", "coral", "MAÑANA", "TERMINA", "Hasta 45% OFF solo hasta el miércoles", "AD_NOV_81"),
    ("V7_ultimo_dia", "lima", "HOY ES EL", "ÚLTIMO DÍA", "Hasta 45% OFF solo por hoy", "AD_NOV_89"),
    ("V8_ultimas_horas", "verde", "ÚLTIMAS", "HORAS", "El Black Friday termina hoy", "AD_NOV_87"),
]


def gradient(top, bottom):
    img = Image.new("RGB", (W, H), top)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return img


def fit_font(path, text, max_w, start, min_size=40):
    size = start
    while size > min_size:
        f = ImageFont.truetype(path, size)
        b = f.getbbox(text)
        if b[2] - b[0] <= max_w:
            return f
        size -= 4
    return ImageFont.truetype(path, min_size)


def star(d, cx, cy, r, fill, outline):
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        rr = r if k % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=fill, outline=outline)


def draw_center(d, text, font, y, fill):
    b = font.getbbox(text)
    w = b[2] - b[0]
    x = (W - w) / 2 - b[0]
    d.text((x, y - b[1]), text, font=font, fill=fill)
    return y + (b[3] - b[1])


def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if font.getlength(t) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    lines.append(cur)
    if len(lines) == 2:  # repartir en dos líneas parejas
        best = None
        for i in range(1, len(words)):
            a, b = " ".join(words[:i]), " ".join(words[i:])
            m = max(font.getlength(a), font.getlength(b))
            if m <= max_w and (best is None or m < best[0]):
                best = (m, [a, b])
        if best:
            lines = best[1]
    return lines


def rounded(im, r):
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1], r, fill=255)
    out = Image.new("RGBA", im.size)
    out.paste(im, (0, 0), mask)
    return out, mask


def make(name, pal, l1, l2, sub, ad):
    top, bot, head, subc, pillbg, pilltx = PALETTES[pal]
    img = gradient(top, bot)
    d = ImageDraw.Draw(img)

    # Pastilla BLACK FRIDAY
    pf = ImageFont.truetype(POP[800], 46)
    label = "BLACK FRIDAY"
    tw = pf.getlength(label)
    pw, ph = tw + 2 * 92, 88
    px, py = (W - pw) / 2, 190
    d.rounded_rectangle([px, py, px + pw, py + ph], ph / 2, fill=pillbg)
    b = pf.getbbox(label)
    d.text(((W - tw) / 2, py + (ph - (b[3] - b[1])) / 2 - b[1]), label, font=pf, fill=pilltx)
    for sx in (px + 48, px + pw - 48):
        star(d, sx, py + ph / 2, 24, (255, 200, 61), (230, 150, 20))

    # Titulares
    y = py + ph + 46
    f1 = fit_font(POP[900], l1, 960, 120)
    y = draw_center(d, l1, f1, y, head) + 26
    f2 = fit_font(FRA[900], l2, 980, 230)
    y = draw_center(d, l2, f2, y, head) + 34

    # Bajada
    fs = ImageFont.truetype(POP[600], 42)
    for line in wrap(sub, fs, 900):
        y = draw_center(d, line, fs, y, subc) + 14
    y += 30

    # Tarjeta con el anuncio 4:5
    ad_img = Image.open(BASE / "ads" / f"{ad}.jpg").convert("RGB")
    max_h = 1700 - y
    cw = min(820, int(max_h * 0.8))
    ch = int(cw * 1.25)
    ad_img = ad_img.resize((cw, ch), Image.LANCZOS)
    card, mask = rounded(ad_img, 38)
    cx = (W - cw) // 2
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle([cx + 6, y + 16, cx + cw + 6, y + ch + 16], 38, fill=(0, 0, 0, 70))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    img = Image.alpha_composite(img.convert("RGBA"), shadow)
    img.paste(card, (cx, y), mask)
    out = OUT / f"{name}.jpg"
    img.convert("RGB").save(out, quality=90, optimize=True)
    return out, (cw, ch, y, y + ch)


if __name__ == "__main__":
    for v in VARIANTS:
        out, info = make(*v)
        print(out.name, info, out.stat().st_size // 1024, "KB")
