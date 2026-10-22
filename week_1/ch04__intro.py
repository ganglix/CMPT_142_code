# Indexing and Slicing of !Sequences!
# str
'computer science'
# list
['apple', 'banana', 'orange', 1.0, 2.0]
# tuple
(1, 2, 3)



# •What is indexing used for?
# •What does a positive index mean?
# •What does a negative index mean?

#         ________
#         87654321
#         01234567
course = 'CMPT 142'
print(course[1])
print(course[7])
# print(course[8]) # ERROR! string index out of range
print(course[-1])  # -1 is not ount of range
print(course[-2])
# print(course[-9])  # ERROR! string index out of range



# --------- take a break -----------

# •What is slicing used for?
# •What are the meanings of the First, second, and third
# numbers in a slicing operation?
text = 'computer science'

# text[start : stop(not included) : step]
print(text[0 : 3 : 1])
print(text[0 : 3 : 2])
print(text[0 : 100 : 1]) # no error out of raneg slicin is OK
# omit:
print(text[: 3 :])  # default start = one end (this case 0), default step = 1
print(text[::])   # from one end to the other end, step = 1
print(text[-7::1]) # from -7 to one end (included)
print(text[-7:100:1]) # from -7 to 100 (out of range)
print(text[::-1]) # from one end to the other, with -1 step
# what if the slice start end step combination does not make sense!
print(text[9:2:1]) # this slide does not make sense as it starts from right and end at left with step 1
print(type(text[9:2:1])) # empty string







# I want to mention omitted value, index out of range, and range of slice
