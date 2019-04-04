from random import randint


class Die:

    def __init__(self, dice_str):
        self.dice_num = int(dice_str[0])
        self.dice_size = int(dice_str[1])
        self.rolls = []

    @property
    def total(self):
        return sum(self.rolls)

    def roll(self):
        self.rolls = [randint(1, self.dice_size) for i in range(self.dice_num)]
        return self

    @property
    def printer(self):
        return print(self.total, self.rolls)


if __name__ == '__main__':
    while True:
        die_str = input().split('d')
        current = Die(die_str).roll().printer

