# Justino & Assunção Advogados

Site do escritório Justino & Assunção Sociedade de Advogados (Uberlândia, MG): uma página central e uma página por área, cada uma pronta para receber tráfego pago.
Estático, sem dependências: `python3 build.py` gera as páginas e a ponte `/obrigado`, que leva ao WhatsApp com a mensagem da área.

O layout veio do site da Ferreira e Dutra Advogados e foi adaptado: preto, marfim e cobre (as cores da logo), a coluna da logo no cabeçalho e no topo, o nome em Montserrat e botões em cobre.

## Páginas
- `/` página central: o escritório, as áreas, os diferenciais, os sócios, como funciona, o alcance e as dúvidas.
- `/familia`, `/inventario`, `/desportivo`, `/marcas`, `/previdenciario`, `/civel`: uma landing por área.
- `/obrigado?c=<botão>&a=<área>`: registra a conversão no `dataLayer` (com o contexto e a área) e abre o WhatsApp com a mensagem daquela área.

## De onde veio cada coisa
- **Textos:** `conteudo.py`, a partir do site atual do escritório (justinoeassuncao.com). Não há promessa de resultado, preço, consulta grátis nem depoimento, por causa do Provimento 205/2021 da OAB. Os prazos e regras legais citados estão marcados com `[REVISAR: prazo legal]` no código.
- **Fotos:** `python3 tools/fotos.py` gera os retratos, os recortes do topo, o ícone da aba e a coluna da logo. Os originais ficam em `assets/src/fotos-ja/` (os arquivos de 14 MB ficam fora do repositório; o script usa as versões `-1800`).
  - Felipe Justino Andrade fica à esquerda, sobre o J; Eduardo Oliveira Assunção à direita, sobre o A.
  - Recorte sem fundo com o Vision da Apple: `swift tools/lift.swift entrada.jpg saida.png`.
- **Fundos:** gerados no ChatGPT (originais em `assets/src/geradas/`). Os `FD-*` vieram do site da Ferreira e Dutra; os `JA-*` foram feitos para este (estádio, sinete de marca, carteira de trabalho e o recorte da colunata para o celular). `python3 tools/fundos.py` gera os WebP.
- **Nome e letras a traço:** `tools/letreiro.py` transforma a Montserrat (licença OFL, em `tools/fontes/`) em contorno SVG.
- **Mapa:** `tools/mapa.py`, contorno do Brasil da Natural Earth (domínio público).
- **Imagem de compartilhamento:** `python3 tools/og.py`, com o servidor local ligado na porta 4236.

## Falta o escritório confirmar (aparece como [A PREENCHER] ou está a conferir)
- Se o (34) 98435-0751 é o WhatsApp (`WHATSAPP` e `TEL_VER` no `build.py`).
- Número da OAB dos dois (`SOCIOS` no `build.py`).
- A grafia do nome do Eduardo: o site antigo escreve "Olivera"; aqui está "Oliveira".
- Um advogado precisa ler as páginas e confirmar os prazos marcados com `[REVISAR: prazo legal]` no `conteudo.py`, principalmente a área previdenciária, que foi escrita sem material do escritório.
- Domínio: depois de ligar, trocar `DOMINIO` e virar `INDEXAR = True`.

## Prévia local
`python3 tools/serve.py 4236`

## Dependências
`pip3 install pillow fonttools`. Para regerar fotos e a imagem de compartilhamento, também `pip3 install playwright numpy` e `playwright install chromium`. O recorte sem fundo só roda no Mac.
