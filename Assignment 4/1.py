import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
from termcolor import colored

paragraph = """At least 13 Palestinians, including three commanders of the militant group Islamic Jihad, have been killed in 
Israeli air strikes on the Gaza Strip.
A Palestinian health official said six women and four children were among the dead. Another 20 people were injured.
Israel said it had launched an operation targeting militants who posed an imminent threat to its citizens.
Islamic Jihad has vowed revenge and Gaza-based militants are expected to respond with rocket fire into Israel.
Correspondents say one significant factor will be the extent to which Hamas, which controls the Strip, joins in.
Israel officials are said to be preparing for days of fighting.
The strikes were the deadliest since three days of fighting between Israel and Islamic Jihad last August."""

words = word_tokenize(paragraph)
pos_tags = pos_tag(words)
ne_tags = ne_chunk(pos_tags)
iob_tags = tree2conlltags(ne_tags)
ne_tree = conlltags2tree(iob_tags)

print("POS: ")
for word, tag in pos_tags:
    if 'NN' in tag:
        print(colored(word, 'red'), end=' ')
    elif 'VB' in tag:
        print(colored(word, 'green'), end=' ')
    else:
        print(word, end=' ')
print('\n')

print("NER: ")
for word, tag, iob in iob_tags:
    if iob == 'B-PERSON':
        print(colored(word, 'yellow'), end=' ')
    elif iob == 'B-GPE' or iob == 'B-LOC':
        print(colored(word, 'green'), end=' ')
    elif iob == 'B-ORG':
        print(colored(word, 'blue'), end=' ')
    else:
        print(word, end=' ')
print('\n')

