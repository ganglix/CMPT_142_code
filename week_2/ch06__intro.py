# creating functions: parameter, arguments, return, (scope)
"""
f(x) = x^2
x is parameter

f(3) = x^2

3 is argument and 3^2 is the return value

"""
def addition(num1,num2):
    total = num1+num2
    return total

print(addition(3,4))


# flowtrace
"""
print(addition(3,4))
_____on a seperate piece of paper--------inside the function-- you can see from outside
____under the hood---------that is what is going on:
    num1 = 3
    num2 = 4
    total = 3 + 4
    return 7
--------------------------------------------------------------
print(7)

"""