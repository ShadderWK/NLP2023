import re
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
import operator

n = 2
test_sentence = "I love X"
sentence = ["I love you!","I love mom.","I love you so much","I love dog.","I love mom so much.","John love you so bad."]

tokens_list = []
for s in sentence:
    tokens = word_tokenize(s.lower())
    tokens = [toks for toks in tokens if re.match("^[a-zA-Z0-9]+$",toks)]
    tokens_list.extend(tokens)

bigrams = ngrams(tokens_list, n)
print()

bigram_list = []
for bigram in list(bigrams):
    if bigram[0] =='love'  :
        bigram_list.append(bigram)
    
finder = BigramCollocationFinder.from_documents(bigram_list)
bigram_measures = nltk.collocations.BigramAssocMeasures()
scored_bigrams = finder.score_ngrams(bigram_measures.raw_freq)


total_count = sum(frequency for bigram, frequency in scored_bigrams)
bigram_prob = {}
for bigram, frequency in scored_bigrams:
    if bigram[0] == "love":
        bigram_prob[bigram] = frequency / total_count

print("bigram prob:", bigram_prob)

prefix = "I love "
suffixes = [bi[1] for bi in scored_bigrams ]
most_probable_suffix = [bi for bi in scored_bigrams if bi[1] >= max(suffixes)]
new_word = most_probable_suffix[0][0][1]
print(f"{test_sentence}: X should be '{new_word}'")

