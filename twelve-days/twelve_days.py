def recite(start_verse, end_verse):
    LINES_AFTER_ONE = [
            "two Turtle Doves, ",
            "three French Hens, ",
            "four Calling Birds, ",
            "five Gold Rings, ",
            "six Geese-a-Laying, ",
            "seven Swans-a-Swimming, ",
            "eight Maids-a-Milking, ",
            "nine Ladies Dancing, ",
            "ten Lords-a-Leaping, ",
            "eleven Pipers Piping, ",
            "twelve Drummers Drumming, "
        ]
    ORDINALS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

    def get_ordinal(index):
        return ORDINALS[index - 1]

    def get_first_line(index):
        return f'On the {get_ordinal(index)} day of Christmas my true love gave to me: '

    def get_lines(index):
        if index == 1:
            return 'a Partridge in a Pear Tree.'
        elif index == 2:
            return LINES_AFTER_ONE[0] + 'and a Partridge in a Pear Tree.'
        elif index > 2 or index <= 12:
            return LINES_AFTER_ONE[index - 2] + get_lines(index - 1)
        else:
            raise Exception(f'{index} is not a valid number of days.')

    def get_verse(start_verse):
        return get_first_line(start_verse) + get_lines(start_verse)

    def get_verses(start_verse, end_verse):
        if start_verse == end_verse:
            return [get_verse(start_verse)]
        else:
            return [get_verse(start_verse), *get_verses(start_verse + 1, end_verse)]
            
    return get_verses(start_verse, end_verse)