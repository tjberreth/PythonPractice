def is_isogram(string):
    alpha_dict = dict()
    for char in string.lower():
        if char.isalpha() and char in alpha_dict:
            return False
        else:
            alpha_dict[char] = None
    return True