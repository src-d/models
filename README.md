source{d} MLonCode models
=========================

## bot-detection
Model that identifies bots from humans among developer identities.

Example:

```python
from sklearn.preprocessing import LabelEncoder
from sourced.ml.models import BotDetection
from xgboost import XGBClassifier

bot_detection = BotDetection.load(bot-detection)
xgb_cls = XGBClassifier()
xgb_cls._Booster = bot_detection_model.booster
xgb_cls._le = LabelEncoder().fit([False, True])
print('model configuration: ', xgb_cls)
print('BPE model vocabulary size: ', len(bot_detection.bpe_model.vocab()))
```

1 model:

* <default> [94806d1f-1995-4c72-89c9-07681fa9d97d](/bot-detection/94806d1f-1995-4c72-89c9-07681fa9d97d.md)

## bow
Weighted bag-of-words, that is, every bag is a feature extracted from source code and associated with a weight obtained by applying TFIDF.

Example:

```python
from sourced.ml.models import BOW
bow = BOW().load(bow)
print("Number of documents:", len(bow))
print("Number of tokens:", len(bow.tokens))
```

4 models:

*  [1e0deee4-7dc1-400f-acb6-74c0f4aec471](/bow/1e0deee4-7dc1-400f-acb6-74c0f4aec471.md)
* <default> [1e3da42a-28b6-4b33-94a2-a5671f4102f4](/bow/1e3da42a-28b6-4b33-94a2-a5671f4102f4.md)
*  [694c20a0-9b96-4444-80ae-f2fa5bd1395b](/bow/694c20a0-9b96-4444-80ae-f2fa5bd1395b.md)
*  [da8c5dee-b285-4d55-8913-a5209f716564](/bow/da8c5dee-b285-4d55-8913-a5209f716564.md)

## docfreq
Document frequencies of features extracted from source code, that is, how many documents (repositories, files or functions) contain each tokenized feature.

Example:

```python
from sourced.ml.models import DocumentFrequencies
df = DocumentFrequencies().load(docfreq)
print("Number of tokens:", len(df))
```

2 models:

*  [55215392-36fc-43e5-b277-500f5b68d0c6](/docfreq/55215392-36fc-43e5-b277-500f5b68d0c6.md)
* <default> [f64bacd4-67fb-4c64-8382-399a8e7db52a](/docfreq/f64bacd4-67fb-4c64-8382-399a8e7db52a.md)

## id2vec
Source code identifier embeddings, that is, every identifier is represented by a dense vector.

Example:

```python
from sourced.ml.models import Id2Vec
id2vec = Id2Vec().load(id2vec)
print("Number of tokens:", len(id2vec))
```

2 models:

*  [3467e9ca-ec11-444a-ba27-9fa55f5ee6c1](/id2vec/3467e9ca-ec11-444a-ba27-9fa55f5ee6c1.md)
* <default> [92609e70-f79c-46b5-8419-55726e873cfc](/id2vec/92609e70-f79c-46b5-8419-55726e873cfc.md)

## id_splitter_bilstm
Model that contains source code identifier splitter BiLSTM weights.

Example:

```python
from sourced.ml.models.id_splitter import IdentifierSplitterBiLSTM
id_splitter = IdentifierSplitterBiLSTM().load(id_splitter_bilstm)
id_splitter.split(identifiers)
```

1 model:

* <default> [522bdd11-d1fa-49dd-9e51-87c529283418](/id_splitter_bilstm/522bdd11-d1fa-49dd-9e51-87c529283418.md)

## topics
Topic modeling of Git repositories. All tokens are identifiers extracted from repositories and seen as indicators for topics. They are used to infer the topic(s) of repositories.

Example:

```python
from sourced.ml.models import Topics
topics = Topics().load(topics)
print("Number of topics:", len(topics))
print("Number of tokens:", len(topics.tokens))
```

1 model:

* <default> [c70a7514-9257-4b33-b468-27a8588d4dfa](/topics/c70a7514-9257-4b33-b468-27a8588d4dfa.md)

## typos_correction
Model that suggests fixes to correct typos.

Example:

```python
from lookout.style.typos.corrector import TyposCorrector
corrector = TyposCorrector().load(typos_correction)
print("Corrector configuration:\n", corrector.dump())
```

2 models:

* <default> [16577a2c-7f17-4a6f-a759-92f3a00cf339](/typos_correction/16577a2c-7f17-4a6f-a759-92f3a00cf339.md)
*  [245fae3a-2f87-4990-ab9a-c463393cfe51](/typos_correction/245fae3a-2f87-4990-ab9a-c463393cfe51.md)
