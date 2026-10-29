a = 3
b = 4
c = 5

print(
    (a+b > c) or not (a > c and a > b)
)

def shoutout():
    print("yes, I was called!")

print(
    (a+b > c) or shoutout()   # True or .... is True anyways no need to check the rest
)



# how does python think about this?
