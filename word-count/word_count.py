import re

def count_words(sentence):
    regex_non_word_characters = re.compile('[^a-zA-Z0-9\']')
    word_counts = dict()
    for word in regex_non_word_characters.split(sentence.lower()):
        stripped_word = word.strip('\'')
        if stripped_word != '':
            word_counts[stripped_word] = word_counts.get(stripped_word, 0) + 1
    return word_counts
