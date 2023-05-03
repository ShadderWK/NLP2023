import nltk
import string

sentence = """Cherry blossom represents the nature of life and a season of renewal in
Japanese culture. Last year, the season attracted nearly five million people and boosted the
economy by about $2.7 billion, according to figures from Bloomberg."""

tokens = nltk.wordpunct_tokenize(sentence)

unigram_list = []
bigram_list = []

exclude = set(string.punctuation)

for i in range(len(tokens)):
    if tokens[i].isalnum() or '.' in tokens[i]:
        if '.' in tokens[i]:
            decimal_parts = tokens[i].split('.')
            if len(decimal_parts) == 2 and all(part.isdigit() for part in decimal_parts):
                unigram_list.extend(decimal_parts)
        else:
            if not any(char in exclude for char in tokens[i]):
                unigram = tokens[i].lower()
                unigram_list.append(unigram)

    if i > 0:
        bigram = (tokens[i-1], tokens[i])
        if all(t.isalnum() or '.' in t for t in bigram) and not any(char in exclude for char in bigram):
            bigram = tuple(t.lower() for t in bigram)
            bigram_list.append(bigram)

print("Unigram =", unigram_list)
print()
print("The 2-gram =",bigram_list)

