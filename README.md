# Classificação de notícias falsas em português (Fake.br)

Projeto da disciplina de Mineração de Texto (Ciência da Computação, UFRPE). O objetivo é comparar classificadores **tradicionais** (TF-IDF com Regressão Logística, SVM e Naive Bayes) com classificadores de **Deep Learning** (BERTimbau e Word2Vec + BiLSTM) na detecção de notícias falsas.

## Antes de começar, leia

- [`GLOSSARY.md`](GLOSSARY.md): vocabulário do projeto (divisão oficial, par alinhado, classe positiva…)
- [`docs/adr/`](docs/adr/): decisões que valem para todo mundo e os motivos de cada uma

## Regras comuns a todos os modelos

1. **Corpus:** Fake.br, apenas o **texto normalizado por tamanho**.
2. **Divisão:** sempre a de `data/split.csv`, carregada com `src.dados.carregar_corpus()`. Ninguém gera a própria divisão.
3. **Conjunto de teste:** só é usado na avaliação final.
4. **Classe positiva:** notícia falsa (`rotulo = 1`).
5. **Saída:** cada modelo salva `resultados/predictions_<modelo>.csv` com as colunas `id, y_true, y_pred, score`, sobre o conjunto de teste. `score` é a probabilidade de a notícia ser falsa.

## Notebooks

| Notebook | Conteúdo |
|---|---|
| `00_divisao_oficial.ipynb` | Gera e verifica a divisão oficial (já executado) |
| `01_tradicionais.ipynb` | TF-IDF + LogReg / SVM / Naive Bayes [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LeanderHeitor/fakebr-classificacao/blob/main/01_tradicionais.ipynb) |
| `02_bertimbau.ipynb` | Fine-tuning do BERTimbau |
| `03_word2vec_bilstm.ipynb` | Word2Vec + BiLSTM |
| `04_comparacao.ipynb` | Métricas finais, teste de McNemar e análise de erros |

## Uso rápido

```python
from src.dados import carregar_corpus
df = carregar_corpus()   # baixa o Fake.br em data/ na primeira vez
treino = df[df.split == "treino"]
```

No Colab, a primeira célula de cada notebook clona este repositório e entra na pasta dele. Para abrir um notebook direto no Colab: *Arquivo → Abrir notebook → GitHub* e cole `LeanderHeitor/fakebr-classificacao`.

## Referências

- Monteiro et al. *Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results*. PROPOR 2018.
- Corpus: https://github.com/roneysco/Fake.br-Corpus
- `referencia/`: notebook disponibilizado pelo professor e anotações da reunião.
