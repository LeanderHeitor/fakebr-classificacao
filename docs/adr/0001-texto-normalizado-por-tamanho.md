# Usar o texto normalizado por tamanho, e não o texto completo

No Fake.br, as notícias verdadeiras têm em média 1.268 tokens e as falsas, 216 (Monteiro et al., 2018, Tabela 3). Com o texto completo, um classificador pode separar as classes pelo comprimento em vez do conteúdo. O paper original reporta 96% de acurácia com bag of words no texto completo e 88% no texto normalizado, e os autores consideram o primeiro resultado "provavelmente enviesado". Decidimos que todos os modelos do projeto (tradicionais e de Deep Learning) usam `size_normalized_texts/`. A comparação também fica mais justa porque o BERTimbau trunca em 512 tokens e enxergaria o tamanho de forma diferente dos modelos TF-IDF.

## Consequências

- A baseline de referência para os modelos tradicionais é **~0,88 de F1/acurácia** (LinearSVC + bag of words booleano, 5-fold CV), e não 0,96.
- O texto completo só pode aparecer como experimento extra, explicitamente rotulado como enviesado pelo tamanho.

Referência: Monteiro, R. A. et al. *Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results*. PROPOR 2018, LNCS 11122, pp. 324–334.
