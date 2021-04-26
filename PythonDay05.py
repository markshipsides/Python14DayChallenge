# MarkS - Python Challenge Day 05 - Keeping It Concise


def squared_list(number_string):
    number_list = [int(x) for x in number_string.split(',')]
    squares_list = [x * x for x in number_list]
    return sum(squares_list)


list_of_numbers = (input("Please enter a list of numbers to square and sum:"))
print("Squared and Summed result = ", squared_list(list_of_numbers))
