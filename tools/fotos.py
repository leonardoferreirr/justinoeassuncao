#!/usr/bin/env python3
"""Retratos dos sócios, recortes do topo e ícone da aba (a imagem de compartilhamento sai do tools/og.py).

    python3 tools/fotos.py

Originais em assets/src/fotos-ja/ (baixados do site atual do escritório, justinoeassuncao.com).
"""
import asyncio, os, sys
from pathlib import Path
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
SRC, OUT, IMG = RAIZ / "assets/src/fotos-ja", RAIZ / "assets/img/fotos", RAIZ / "assets/img"
CH = os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-1234/chrome-headless-shell-mac-arm64/chrome-headless-shell")
CH = CH if os.path.exists(CH) else None   # sem esse caminho, usa o Chromium padrão do Playwright
sys.path.insert(0, str(RAIZ / "tools"))

# (arquivo, nome, topo do recorte 4:5 em fração da altura que sobra)
RETRATOS = [("felipe-1800.jpg", "felipe", .04), ("eduardo-1800.jpg", "eduardo", .04)]
# Recortes sem fundo para o topo (Vision da Apple, só no Mac: swift tools/lift.swift entrada.jpg saida.png)
# (arquivo, nome, altura do busto em fração do recorte, contração da borda em px, como "contrair seleção" do Photoshop)
# Os dois vêm cortados na cintura, na mesma proporção (Felipe Justino sobre o J, Eduardo Assunção sobre o A).
RECORTES = [("felipe-recorte.png", "felipe-recorte", .7, 7), ("eduardo-recorte.png", "eduardo-recorte", .7, 7)]


def salvar(im, nome, larguras, q=80):
    for w in larguras:
        alvo, w = w, min(w, im.width)
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(OUT / f"{nome}-{alvo}.webp", "WEBP", quality=q, method=6)


def retratos():
    OUT.mkdir(parents=True, exist_ok=True)
    for arq, nome, ancora in RETRATOS:
        im = Image.open(SRC / arq).convert("RGB")
        W, H = im.size
        if W * 1.25 <= H:
            w, h = W, round(W * 1.25)
        else:
            w, h = round(H * .8), H
        x0, y0 = (W - w) // 2, round((H - h) * ancora)
        salvar(im.crop((x0, y0, x0 + w, y0 + h)), nome, (480, 720, 960))
    for arq, nome, busto, contrai in RECORTES:
        im = Image.open(SRC / arq).convert("RGBA")
        # contrai a borda (some a franja branca do fundo antigo) e suaviza 1 px
        a = im.getchannel("A").filter(ImageFilter.MinFilter(contrai)).filter(ImageFilter.GaussianBlur(1.1))
        im.putalpha(a)
        # versão para fundo claro (seção "Quem cuida do seu caso"): só a contração, sem escurecer a borda
        claro = im.crop(im.getbbox())
        claro = claro.crop((0, 0, claro.width, round(claro.height * busto)))
        for alvo in (560, 900):
            alt = min(alvo, claro.height)
            claro.resize((round(claro.width * alt / claro.height), alt), Image.LANCZOS).save(
                OUT / f"{nome}-claro-{alvo}.webp", "WEBP", quality=82, method=6)
        # borda semitransparente puxada para o escuro: o que restou do fundo claro não vira halo sobre o grafite
        import numpy as np
        px = np.asarray(im).astype(np.float32)
        k = .7 + .3 * (px[..., 3:4] / 255)
        px[..., :3] *= k
        im = Image.fromarray(px.clip(0, 255).astype(np.uint8))
        im = im.crop(im.getbbox())
        im = im.crop((0, 0, im.width, round(im.height * busto)))
        for alvo in (560, 900):                    # o nome segue o pedido; o tamanho real não passa do original
            alt = min(alvo, im.height)
            w = round(im.width * alt / im.height)
            im.resize((w, alt), Image.LANCZOS).save(OUT / f"{nome}-{alvo}.webp", "WEBP", quality=82, method=6)


async def icones():
    """Ícone da aba e do iPhone: a coluna com o JA da logo do escritório, em bronze."""
    logo = Image.open(SRC / "logo.png").convert("RGBA")
    px = logo.load()
    for y in range(logo.height):              # o fundo da logo é preto: vira transparente pela luminosidade
        for x in range(logo.width):
            r, g, b, a = px[x, y]
            lum = max(r, g, b)
            px[x, y] = (r, g, b, min(255, int(lum * 2.2)))
    logo = logo.crop(logo.getbbox())
    lado = max(logo.size); q = Image.new("RGBA", (lado, lado), (0, 0, 0, 0)); q.alpha_composite(logo, ((lado - logo.width) // 2, (lado - logo.height) // 2))
    q.resize((64, 64), Image.LANCZOS).save(IMG / "favicon-ja.png")
    fundo = Image.new("RGBA", (180, 180), (12, 12, 13, 255)); m = q.resize((124, 124), Image.LANCZOS); fundo.alpha_composite(m, (28, 28))
    fundo.convert("RGB").save(IMG / "apple-touch-icon.png")
    q.save(RAIZ / "assets/src/fotos-ja/coluna.png")


if __name__ == "__main__":
    retratos()
    asyncio.run(icones())
    print("ok:", sorted(p.name for p in OUT.glob("*.webp")))
