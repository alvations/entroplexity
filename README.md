# Entroplexity

**Sense Entropy**: https://gist.github.com/alvations/bf7c941a9748585c3aea

**Sentence Perplexity**: Language Model score (see https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf)


```bash
# Download wikipedia-complex.zip from  https://drive.google.com/open?id=0B04oQzUfrOTjSGdsTl9QbUJqczg
unzip wikipedia-complex.zip
# Build the language model.
~/mosesdecoder/bin/lmplz -o 5 < WIKI_complex > wiki.arpa
~/kenlm/bin/build_binary wiki.arpa wiki.kenlm

# Extract sense entropy
python entro.py cwi_inputs.lemmatized.txt > sense-entropy.train
python entro.py cwi_test.lemmatized.txt > sense-entropy.test

# Extract sentence perplexity
python perplexity.py cwi_inputs.txt wiki.kenlm > sent-perplexity.train
python perplexity.py cwi_test.txt wiki.kenlm > sent-perplexity.test

python entroplexity_classify.py
```

# Cite

Jose Manuel Martinez Martinez and Liling Tan. Complex Word Identification with Sense Entropy and Sentence Perplexity. In SemEval-2016. 

```

```
