# Define a Python function called format_price that:
# (a) Has two integer parameters, indicating the cost in dollars
# and cents of an item
# (b) Returns a single string in the format "$D.C".
# (c) Example: if called with arguments 9 and 99, the function
# should return the string $9.99

def format_price(dollar, cent):
    """
    It takes two numbers, dollar and cent, and return the formatted price
    dollar: int, the dollar amount
    cent: int, the cent amount
    return: str, the formatted price $dd.cc
    """
    formatted = "$" + str(dollar) + "." + str(cent)
    return formatted

print(format_price(9, 99))

# recommended: (main code)
d = input("What's your dollar? ")
c = input("What's your cent? ")
formatted_price = format_price(d, c)
print(formatted_price)


# follow up on types of functions


# with parameters, but no return
def print_format_price(dollar, cent):
    formatted = "$" + str(dollar) + "." + str(cent)
    print(formatted)

whatsreturned = print_format_price(10, 10)
print( type(print(whatsreturned)) )   # print() does not return anything

# no parameter, no return

def display_format_price():
    dollar = input("What's your dollar? ")
    cent = input("What's your cent? ")
    formatted = "$" + dollar + "." + cent
    print(formatted)

display_format_price()  # no arguments, no return