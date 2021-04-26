# MarkS - Python Challenge Day 05 - Keeping It Concise


def squared_list(number_string):
    squares_list = [int(x) * int(x) for x in number_string.split(',')]
    return sum(squares_list)


list_of_numbers = (input("Please enter a list of numbers to square and sum:"))
print("Squared and Summed result = ", squared_list(list_of_numbers))
