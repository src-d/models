source{d} MLonCode models
=========================

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
