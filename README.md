# NLP Tokenization & Byte Pair Encoding (BPE) Assignment

**Student Name:** Laharika Dattu  
**Student ID:** 700788001  
**Course:** Natural Language Processing

---

## 1. Objective

This assignment demonstrates:

1. Different tokenization approaches in NLP:  
   - Naive space-based  
   - NLTK tokenizer  
   - spaCy tokenizer  

2. Byte Pair Encoding (BPE) merges on a toy corpus.

---

## 2. Tokenization Explanation

### a) Naïve Space-Based Tokenization
- Splits the text based on spaces.
- Issues:
  - Punctuation remains attached (`today.`)
  - Contractions are not split (`Don’t`)

### b) NLTK Tokenizer
- Uses the Punkt tokenizer.
- Separates punctuation and splits contractions (`Don't` → `Do` + `n't`).

### c) spaCy Tokenizer
- Handles punctuation, contractions, and Unicode characters robustly.
- Differences compared to NLTK:
  - Slight variations in handling special Unicode apostrophes.

---

## 3. Byte Pair Encoding (BPE)

### Steps:

1. Add an end-of-word marker `_`.
2. Count all consecutive character pairs (bigrams).
3. Merge the most frequent bigram.
4. Repeat for 5 iterations.
5. Update vocabulary after each merge.

**Purpose:** Reduce corpus size and generate subword units for NLP models.

---

## Troubleshooting:
1. Missing libraries, started with installing pip:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

2. Missing nltk libraries, imported all.
* Goto python shell:
```
import nltk
nltk.download('all')
```
3. Ran into certification issues:
```
[nltk_data] Error loading all: <urlopen error [SSL: [nltk_data] CERTIFICATE_VERIFY_FAILED] certificate verify failed: [nltk_data] unable to get local issuer certificate (_ssl.c:1028)> False
```

For this, run the MacOS certificate installer in terminal:
```
/Applications/Python\ 3.13/Install\ Certificates.command
```

4. Then, ran into spacy library issues, like below:
```
OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a Python package or a valid path to a data directory.
```

For this, installed the required library.
```
python3 -m spacy download en_core_web_sm
```

