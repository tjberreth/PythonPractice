class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '') if card_num else ''

    def valid(self):
        def double_and_wrap(value):
            doubled = value * 2
            return doubled if doubled < 10 else doubled - 9

        if len(self.card_num) < 2 or not self.card_num.isnumeric():
            return False
        else:
            return sum([int(num) if index % 2 == 0 else double_and_wrap(int(num)) for index, num in enumerate(reversed(self.card_num))]) % 10 == 0

