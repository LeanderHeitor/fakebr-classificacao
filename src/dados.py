"""Acesso ao corpus Fake.br e à divisão oficial do projeto.

Uso em qualquer notebook (local ou Colab, a partir da raiz do repositório):

    from src.dados import carregar_corpus
    df = carregar_corpus()                       # todas as 7.200 notícias
    treino = df[df.split == "treino"]

Colunas: id, par, rotulo (1 = falsa, 0 = verdadeira), categoria, split, texto.
O texto é sempre a versão normalizada por tamanho (ver docs/adr/0001).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
DIR_CORPUS = RAIZ / "data" / "Fake.br-Corpus"
ARQ_SPLIT = RAIZ / "data" / "split.csv"
URL_CORPUS = "https://github.com/roneysco/Fake.br-Corpus.git"

SEMENTE = 42
PROPORCOES = {"treino": 0.70, "validacao": 0.15, "teste": 0.15}
ROTULOS = {"fake": 1, "true": 0}


def baixar_corpus() -> Path:
    """Clona o Fake.br em data/ se ainda não existir."""
    if not DIR_CORPUS.exists():
        DIR_CORPUS.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--depth", "1", "-q", URL_CORPUS, str(DIR_CORPUS)],
            check=True,
        )
    return DIR_CORPUS


def _ler(caminho: Path) -> str:
    return caminho.read_text(encoding="utf-8").strip()


def _listar_noticias() -> pd.DataFrame:
    """Uma linha por notícia, sem o texto e sem a divisão."""
    base = baixar_corpus()
    linhas = []
    for classe, rotulo in ROTULOS.items():
        for arq in (base / "size_normalized_texts" / classe).glob("*.txt"):
            par = int(arq.stem)
            meta = base / "full_texts" / f"{classe}-meta-information" / f"{par}-meta.txt"
            # Os pares 697 e 1468 de size_normalized_texts não têm metadados
            # correspondentes em full_texts (inconsistência do próprio corpus).
            categoria = (
                meta.read_text(encoding="utf-8").splitlines()[2].strip()
                if meta.exists()
                else "desconhecida"
            )
            linhas.append(
                {"id": f"{classe}_{par}", "par": par, "rotulo": rotulo, "categoria": categoria}
            )
    return pd.DataFrame(linhas).sort_values(["par", "rotulo"]).reset_index(drop=True)


def gerar_divisao() -> pd.DataFrame:
    """Gera a divisão oficial por par alinhado (docs/adr/0002). Rode uma vez só."""
    df = _listar_noticias()
    pares = np.sort(df["par"].unique())
    rng = np.random.default_rng(SEMENTE)
    rng.shuffle(pares)

    n = len(pares)
    n_treino = round(n * PROPORCOES["treino"])
    n_val = round(n * PROPORCOES["validacao"])
    destino = {}
    for i, par in enumerate(pares):
        destino[par] = "treino" if i < n_treino else "validacao" if i < n_treino + n_val else "teste"

    df["split"] = df["par"].map(destino)
    return df


def carregar_corpus() -> pd.DataFrame:
    """Corpus completo com a divisão oficial e o texto normalizado por tamanho."""
    if not ARQ_SPLIT.exists():
        raise FileNotFoundError(
            f"{ARQ_SPLIT} não existe. Ele deve vir versionado no repositório; "
            "não gere uma divisão nova por conta própria."
        )
    base = baixar_corpus()
    df = pd.read_csv(ARQ_SPLIT)
    df["texto"] = [
        _ler(base / "size_normalized_texts" / i.split("_")[0] / f"{i.split('_')[1]}.txt")
        for i in df["id"]
    ]
    return df
