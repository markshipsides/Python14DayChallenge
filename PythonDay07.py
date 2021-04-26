# MarkS - Python Challenge Day 07 -  SlackAdder


def slack_adder(integer_numbers, target_integer):
    list_length = len(integer_numbers)
    for i in range(list_length):
        for j in range(i+1, list_length):
            if integer_numbers[i] + integer_numbers[j] == target_integer:
                return i, j


numbers: list = [11, 7, 2, 15]
target: int = 9

print(slack_adder(numbers, target))
