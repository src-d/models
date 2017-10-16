source{d} MLoSC models
======================

## docfreq
Document frequencies of source code identifiers, that is, how many projects contain an identifier.

Example:

```
from ast2vec import DocumentFrequencies
df = DocumentFrequencies().load()
print("Number of tokens:", len(df))
```

1 model:

* <default> [f64bacd4-67fb-4c64-8382-399a8e7db52a](/docfreq/f64bacd4-67fb-4c64-8382-399a8e7db52a.md) 

## id2vec
Source code identifier embeddings, that is, every identifier is represented by a dense vector.

Example:

```
from ast2vec import Id2Vec
id2vec = Id2Vec().load()
print("Number of tokens:", len(id2vec))
```

1 model:

* <default> [92609e70-f79c-46b5-8419-55726e873cfc](/id2vec/92609e70-f79c-46b5-8419-55726e873cfc.md) 

## nbow
Weighted bag-of-words where every word is a dense vector.

Example:

```
from ast2vec import NBOW
nbow = NBOW().load()
print("Number of bags:", len(nbow))
```

1 model:

* <default> [1e3da42a-28b6-4b33-94a2-a5671f4102f4](/nbow/1e3da42a-28b6-4b33-94a2-a5671f4102f4.md) 

## topics
Topic modeling of Git repositories.

Example:

```
from ast2vec import Topics
topics = Topics().load()
print("Number of topics:", len(topics))
```

1 model:

* <default> [c70a7514-9257-4b33-b468-27a8588d4dfa](/topics/c70a7514-9257-4b33-b468-27a8588d4dfa.md) 
