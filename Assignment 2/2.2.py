import nltk

def edit_distance(str1, str2):
    edit_distance_matrix = nltk.edit_distance(str1, str2, substitution_cost=2)
    return edit_distance_matrix

# Input
str1 = input('Str1: ')
str2 = input('Str2: ')
print('The edit distance of {} and {} is {}'.format(str1,str2,edit_distance(str1, str2)))

