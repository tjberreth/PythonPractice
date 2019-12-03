import functools
import re

def abbreviate(words):
    def first_letter(word):
        return next((x for x in word if x.isalpha()), '')
    split_regex = re.compile('[\s-]')
    return ''.join(list(map(first_letter, split_regex.split(words)))).upper()
