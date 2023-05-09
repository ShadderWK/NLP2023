import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.chunk.util import conlltags2tree, tree2conlltags
from termcolor import colored

# Sample paragraph
with open('paragraph.txt','r') as file :
    paragraph = file.read()

# Tokenize paragraph into words
words = word_tokenize(paragraph)

# Perform Part-of-Speech tagging on words
pos_tags = pos_tag(words)

# Perform Named Entity Recognition on tagged words
ne_tags = ne_chunk(pos_tags)

# Convert the tags to IOB format
iob_tags = tree2conlltags(ne_tags)

# Convert the IOB format tags to a tree
ne_tree = conlltags2tree(iob_tags)

# Loop through words and tags and print with colored output
print("POS: ")
for word, tag in pos_tags:
    if 'NN' in tag:
        print(colored(word, 'red'), end=' ')
    elif 'PERSON' in tag:
        print(colored(word, 'red'), end=' ')
    elif 'GPE' in tag or 'LOC' in tag:
        print(colored(word, 'blue'), end=' ')
    elif 'ORG' in tag:
        print(colored(word, 'green'), end=' ')
    elif 'VB' in tag:
        print(colored(word, 'green'), end=' ')
    else:
        print(word, end=' ')
print('\n')

# Loop through named entities and print with colored output
print("NER: ")
for word, tag, iob in iob_tags:
    if iob == 'B-PERSON':
        print(colored(word, 'yellow'), end=' ')
    elif iob == 'B-GPE' or iob == 'B-LOC':
        print(colored(word, 'green'), end=' ')
    elif iob == 'B-ORG':
        print(colored(word, 'blue'), end=' ')
    elif iob == 'B-VP':
        print(colored(word, 'magenta'), end=' ')
    else:
        print(word, end=' ')
print('\n')