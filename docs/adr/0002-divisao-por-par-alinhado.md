# Dividir o corpus por par alinhado, e não por notícia

Cada notícia falsa do Fake.br tem uma notícia verdadeira "irmã" sobre o mesmo assunto (mesmo número de arquivo). Com um `train_test_split` comum, as duas notícias de um par podem cair em conjuntos diferentes. Nesse caso o modelo vê o assunto rotulado no treino e é avaliado na irmã, o que mistura memória de tema com detecção de notícia falsa. Decidimos que a divisão oficial (70% treino, 15% validação, 15% teste, `random_state=42`) é feita por par: as duas notícias de um par sempre ficam no mesmo conjunto. A validação cruzada interna dos modelos tradicionais usa `GroupKFold` com o mesmo agrupamento.

## Consequências

- Cada conjunto sai automaticamente balanceado, com 50% de falsas e 50% de verdadeiras, sem precisar de estratificação.
- Todos os modelos leem a divisão de `data/split.csv`. Nenhum notebook gera a própria divisão.
- Os resultados não são diretamente comparáveis aos do paper original, que usou 5-fold CV sem agrupamento por par.
