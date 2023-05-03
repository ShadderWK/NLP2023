from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re
import nltk

with open('news.txt','r') as file :
    news = file.read()

tokens = nltk.word_tokenize(news)
filtered_words = [tokens for tokens in tokens if len(tokens) >= 3 and all(c.isalpha() for c in tokens)]
freq_dist = FreqDist(filtered_words)

print(f"The number of sentences: {len(sent_tokenize(news))}")
for word, frequency in freq_dist.most_common(10):
    print(f"'{word}', {frequency}")

