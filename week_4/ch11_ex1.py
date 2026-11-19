"""
Exercise 1:
Apply the algorithm-pseudocode-code workflow:
Given a list of numbers, compute how many
numbers are above the average

"""
# algorithm
"""
calculate the total
calculate the average
count how many numbers are above the average
"""

# pseudocode
"""
Function
input: a list of numbers
output: number of numbers above the average

total = 0
for every number in the list:
    add to total
average =  total / number of numbers in the list

count how many numbers are above the average
count = 0
for every number in the list:
    if that number > average:
    count += 1
"""

# code
def above_average(number_list):
    """
    compute how many numbers are above the average for a given list of numbers
    :param number_list: a list of numbers
    :return: number of numbers above the average
    """
    # calculate the total
    total = 0
    for number in number_list:
        total += number   # total = total + number

    # calculate the average
    average =  total / len(number_list)

    # count how many numbers are above the average
    count = 0
    for number in number_list:
        if number > average:
            count += 1

    return count

L = [1,2,3,4,5]
print(above_average(L))
