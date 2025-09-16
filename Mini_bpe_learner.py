from collections import Counter, defaultdict

# Toy corpus
corpus = ["low", "low", "low", "low", "low", "lowest", "lowest",
          "newer", "newer", "newer", "newer", "newer", "newer",
          "wider", "wider", "wider", "new", "new"]

# Add end-of-word marker
corpus = [list(word) + ["_"] for word in corpus]

def get_stats(corpus):
    pairs = Counter()
    for word in corpus:
        for i in range(len(word)-1):
            pairs[(word[i], word[i+1])] += 1
    return pairs

def merge_pair(pair, corpus):
    new_corpus = []
    bigram = "".join(pair)
    for word in corpus:
        w = []
        i = 0
        while i < len(word):
            if i < len(word)-1 and (word[i], word[i+1]) == pair:
                w.append(bigram)
                i += 2
            else:
                w.append(word[i])
                i += 1
        new_corpus.append(w)
    return new_corpus

# Perform 5 BPE merges
vocab = set(char for word in corpus for char in word)
for i in range(5):
    pairs = get_stats(corpus)
    if not pairs:
        break
    best = max(pairs, key=pairs.get)
    corpus = merge_pair(best, corpus)
    vocab.add("".join(best))
    print(f"Step {i+1}, merge {best} → {''.join(best)}, vocab size {len(vocab)}")
