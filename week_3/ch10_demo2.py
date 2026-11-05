# Up until now, only immutable data types have been passed
# as arguments to functions. What happens when we pass
# mutable data?
# Let us observe the effect on an input variable before,
# during, and after a function call that changes the value.


def appendage(minilist, x):
    minilist.append(42)
    x = x + 5
    return minilist


L = [10, 20, 30]
x = 50
list_returned = appendage(L, x)
print(L)   # L's [] in the global scopt does not change, but what's in it can change
print(x)   # x in the global scope does not change
print(list_returned)

# checck if L and list_returned refer to the same list
L.append('new thing')
print(L)
print(list_returned)

# conclusion L and list_returned are the same list, but just different name


# -----------------------------------------
# # does this operation create a new list? YES
# .copy()
# [i for i in oldlist]

