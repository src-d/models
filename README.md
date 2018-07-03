source{d} MLonCode models
=========================

## bow
Weighted bag-of-words, that is, every bag is a feature extracted from source code and associated with a weight obtained by applying TFIDF.

Example:

```
from sourced.ml.models import BOW
bow = BOW().load(bow)
print("Number of documents:", len(bow))
print("Number of tokens:", len(bow.tokens))
```

1 model:

* <default> [1e3da42a-28b6-4b33-94a2-a5671f4102f4](/bow/1e3da42a-28b6-4b33-94a2-a5671f4102f4.md)

## docfreq
Document frequencies of features extracted from source code, that is, how many documents (repositories, files or functions) contain each tokenized feature.

Example:

```
from sourced.ml.models import DocumentFrequencies
df = DocumentFrequencies().load(docfreq)
print("Number of tokens:", len(df))
```

1 model:

* <default> [f64bacd4-67fb-4c64-8382-399a8e7db52a](/docfreq/f64bacd4-67fb-4c64-8382-399a8e7db52a.md)

## topics
Topic modeling of Git repositories. All tokens are identifiers extracted from repositories and seen as indicators for topics. They are used to infer the topic(s) of repositories.

Example:

```
from sourced.ml.models import Topics
topics = Topics().load(topics)
print("Number of topics:", len(topics))
print("Number of tokens:", len(topics.tokens))
```

1 model:

* <default> [c70a7514-9257-4b33-b468-27a8588d4dfa](/topics/c70a7514-9257-4b33-b468-27a8588d4dfa.md)
