# Write a Python function that accepts string parameter s and
# prints whether s has an even or odd amount of characters.
# Sample function console output:
# "Dog" has an odd number of characters.

def check_even(s):
    """
    check if a string has an even or odd amount of characters, and print it out
    s: string, input string
    return: None
    """
    if len(s) % 2 == 0:
        print(s, "has even number of characters")
    else:
        print(s, "has odd number of characters")

check_even("Dog")