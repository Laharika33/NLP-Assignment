
# pip install spacy nltk
# python -m spacy download en_core_web_sm
# ---------------------------

import spacy          # For advanced NLP tokenization (handles punctuation, contractions)
import nltk           # Natural Language Toolkit for basic NLP tasks
from nltk.tokenize import word_tokenize   # NLTK's standard word tokenizer


# Paragraph to test

text = "The weather is nice today. However, it might rain later, so carry an umbrella. Don’t forget to stay hydrated!"


# 1. Naïve space-based tokenization

# Here we simply split the text by spaces.
# This is the simplest form of tokenization but it doesn't handle punctuation or contractions well.
naive_tokens = text.split()
print("Naïve space-based tokenization:")
print(naive_tokens)
print()
# Expected issues:
# - 'today.' includes the period.
# - 'Don’t' remains as one token (not split into Do + n't)
# - Commas and exclamation marks stay attached to words.


# 2. NLTK tokenizer

# NLTK's word_tokenize uses the Punkt tokenizer which is trained to handle punctuation and English contractions.
# It separates punctuation from words and splits contractions like "Don't" -> ["Do", "n't"].
nltk_tokens = word_tokenize(text)
print("NLTK Tokenization:")
print(nltk_tokens)
print()


# 3. spaCy tokenizer

# spaCy's tokenizer is more advanced. It handles:
# - Punctuation separation
# - Contractions (e.g., "Don’t" -> ["Do", "n't"])
# - Unicode characters correctly
# We first load the English language model, then process the text with it.
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
spacy_tokens = [token.text for token in doc]  # Extract tokens as a list of strings
print("spaCy Tokenization:")
print(spacy_tokens)
print()


# 4. Comparison between NLTK and spaCy.
#We loop through the tokens from both tools and highlight positions where they differ.
# Differences may occur due to:
# - Different handling of apostrophes or Unicode characters
# - Slight differences in punctuation splitting
print("Differences:")
for i, (nltk_t, spacy_t) in enumerate(zip(nltk_tokens, spacy_tokens)):
    if nltk_t != spacy_t:
        print(f"Position {i}: NLTK -> {nltk_t} | spaCy -> {spacy_t}")
