# Classify the loops in these Python excerpts as terminating
# (reaches an end) or infinite in nature:

# # (a)
# for x in range(100, 10, 10): # this range is empty
#     print(x * 5)

# (b)
# total = 0
# i = 0
# while i < 10:
#     total = total + i


# (c)
# x = 5
# goal = 16
# while x != goal:
#     x = x + 2


# (d)
divisor = 2
dividend = 49
while dividend % divisor != 0:
    divisor = divisor + 1

def check_prime(num):
    """
    check whether num is prime
    :param num: int, the number to be checked
    :return: boolean, True if num is prime, False otherwise
    """
    divisor = 2
    dividend = num
    while dividend % divisor != 0:
        divisor = divisor + 1
    if divisor == dividend: # only can be devided by itself
        return True
    else:
        print(f'{dividend} can be at least divided by {divisor}')
        return False

# print(check_prime(7979719373))




# (e)
low = -100
high = 100
msg = " Enter int between " + str(low) + " to " + str(high) + ":"
num = int(input(msg))
while num >= low or num <= high:
# while num >= low and num <= high:
    num = int(input(msg))
