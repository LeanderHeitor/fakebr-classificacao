# Glossário — Classificação de notícias falsas (Fake.br)

## Corpus
O Fake.br: 7.200 notícias em português brasileiro, 3.600 falsas e 3.600 verdadeiras, organizadas em pares alinhados. Único corpus do projeto; os textos usados são os normalizados por tamanho.

## Notícia falsa
Notícia rotulada como falsa no corpus. É a **classe positiva**: precisão, revocação e F1 sem qualificação referem-se a ela.
_Evitar:_ "fake" e "spam" (herança do notebook de referência).

## Notícia verdadeira
Notícia rotulada como verdadeira no corpus. Classe negativa.

## Variante de pré-processamento
Uma forma de transformar o texto antes da vetorização. O projeto compara duas: **texto limpo** (minúsculas, sem pontuação e números) e **texto lematizado** (texto limpo, lematizado e sem stopwords).

## Divisão oficial
Partição única e fixa do corpus em **treino**, **validação** e **teste**, usada por todos os modelos do projeto (tradicionais e de Deep Learning). Garante que as comparações entre abordagens sejam justas. A unidade de divisão é o **par alinhado**: as duas notícias de um par sempre caem no mesmo conjunto.
_Evitar:_ "split do meu notebook", divisões geradas por modelo.

## Conjunto de teste
Parte da divisão oficial reservada exclusivamente para a avaliação final. Nenhuma decisão de modelagem (escolha de hiperparâmetros, pré-processamento) pode usá-lo.
_Evitar:_ usar "teste" para a validação.

## Conjunto de validação
Parte da divisão oficial usada para decisões de modelagem e early stopping antes da avaliação final.

## Par alinhado
Uma notícia falsa e uma notícia verdadeira do corpus que tratam do mesmo assunto. O Fake.br é composto por 3.600 pares alinhados.

## Texto normalizado por tamanho
Versão de uma notícia em que, dentro do seu par alinhado, o texto mais longo foi truncado para ter o mesmo número de palavras que o mais curto. Existe para impedir que o classificador aprenda a distinguir as classes pelo comprimento do texto.
_Evitar:_ "texto normalizado" sem qualificação (confunde com normalização de caixa, acentos ou lematização).

## Categoria
Assunto da notícia segundo os metadados do corpus (política, TV & celebridades, sociedade & cotidiano, ciência & tecnologia, economia, religião). Usada na análise de erros.

## Texto completo
Versão original da notícia, sem truncamento.

## Grupo tradicional
Os classificadores baseados em TF-IDF: Regressão Logística, SVM linear e Naive Bayes Multinomial.
_Evitar:_ "ML clássico" com escopo indefinido (não inclui RF, KNN, AdaBoost, XGB).

## Grupo de Deep Learning
Os classificadores neurais do projeto: BERTimbau com fine-tuning e Word2Vec + BiLSTM.
