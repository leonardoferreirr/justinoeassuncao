#!/usr/bin/env python3
"""Fundos gerados no ChatGPT (originais em assets/src/geradas/, código no nome) -> assets/img/fundos/*.webp

    python3 tools/fundos.py

16:9 para o computador (<nome>-<largura>.webp) e 4:5 para o celular (<nome>-m-<largura>.webp).
Quando não há versão 4:5, o celular usa o recorte central da 16:9 (o site faz isso com object-position).
"""
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
SRC, OUT = RAIZ / "assets/src/geradas", RAIZ / "assets/img/fundos"

FUNDOS = {  # nome no site: (16:9, 4:5 ou None). Os FD-* vieram do site da Ferreira e Dutra; os JA-* foram gerados para este.
    "inicio": ("FD-AD", "JA-ADM"),           # colunata ao entardecer: conversa com a coluna da logo (capa da central e chamada final)
    "manifesto": ("FD-M1", "FD-M1M"),        # chuva na janela à noite
    "alcance": ("FD-A2", "FD-A2M"),          # território à noite visto do alto ("de Uberlândia para todo o Brasil")
    "familia": ("FD-FA", None),              # sala de casa ao entardecer, desfocada
    "inventario": ("FD-IN", None),           # chave antiga sobre documentos
    "desportivo": ("JA-DE", None),           # estádio vazio à noite, a bola na marca do pênalti
    "marcas": ("JA-MA", None),               # sinete de latão e caixas sem rótulo na mesa
    "previdenciario": ("JA-PR", None),       # mãos sobre a carteira de trabalho e documentos
    "civel": ("FD-CV", None),                # contratos e caneta na mesa
}


def salvar(im, base, larguras, q=72):
    for w in larguras:
        alvo, w = w, min(w, im.width)
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(OUT / f"{base}-{alvo}.webp", "WEBP", quality=q, method=6)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    feitos = []
    for nome, (larga, alta) in FUNDOS.items():
        arq = SRC / f"{larga}.png"
        if not arq.exists():
            print(f"  ! falta {arq.name}")
            continue
        salvar(Image.open(arq).convert("RGB"), nome, (960, 1600))
        feitos.append(nome)
        if alta and (SRC / f"{alta}.png").exists():
            im = Image.open(SRC / f"{alta}.png").convert("RGB")
            W, H = im.size                       # garante 4:5 exato
            h = round(W * 1.25)
            if h <= H:
                im = im.crop((0, (H - h) // 2, W, (H - h) // 2 + h))
            else:
                w = round(H * .8); im = im.crop(((W - w) // 2, 0, (W - w) // 2 + w, H))
            salvar(im, f"{nome}-m", (640, 900))
    print("ok:", feitos)


if __name__ == "__main__":
    main()
