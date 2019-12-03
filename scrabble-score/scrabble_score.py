import functools
import operator

letters_to_score_list = [
    (['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'], 1),
    (['d', 'g'], 2),
    (['b', 'c', 'm', 'p'], 3),
    (['f', 'h', 'v', 'w', 'y'], 4),
    (['k'], 5),
    (['j', 'x'], 8),
    (['q', 'z'], 10)
]

def letters_to_score_list_to_map(letters_to_score_list):
    letters_to_score_map = dict()
    for letters, score in letters_to_score_list:
        for letter in letters:
            letters_to_score_map[letter] = score
    return letters_to_score_map

letters_to_score_map = letters_to_score_list_to_map(letters_to_score_list)

def score(word):
    return functools.reduce(operator.add, map(letters_to_score_map.get, word.lower()), 0)
