import nltk


def correct_sentence(sentence, dictionary):
    words = sentence.split()
    corrected_words = []

    for word in words:
        corrected_word = correct_spelling(word, dictionary)
        corrected_words.append(corrected_word)

    corrected_sentence = " ".join(corrected_words)
    return corrected_sentence


def correct_spelling(word, dictionary):
    min_distance = len(word)
    closest_word = word

    for w in dictionary:
        distance = nltk.edit_distance(word, w)
        if distance < min_distance:
            min_distance = distance
            closest_word = w

    if min_distance == 0:
        return word
    else:
        return closest_word

with open("dictionary.txt") as file:
    dictionary = file.read().splitlines()


misspelled_sentence = "I opan a bax ant reed a leter"
corrected_sentence = correct_sentence(misspelled_sentence, dictionary)

misspelled_words = misspelled_sentence.split()
corrected_words = corrected_sentence.split()

for i in range(len(misspelled_words)):
    if misspelled_words[i] != corrected_words[i]:
        print(f"{misspelled_words[i]} can be replaced by ('{corrected_words[i]}', 1)")
    else:
        print(f"{misspelled_words[i]} can be replaced by ('{misspelled_words[i]}', 0)")

print()
print(f"Mispelled sentence is >>  {misspelled_sentence}")
print(f"New sentence is       >>  {corrected_sentence}")

