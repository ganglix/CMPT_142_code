
#    _______
#    7654321
#    0123456
s = "Fiction"
print(s[0:len(s):2])


#    ___________
#    BA987654321
#    0123456789A        note: A is 10    B is 11
s = "Green Arrow"

# (a) the first five characters of s, i.e. "Green"
print(s[0:5:])
print(s[0:5])
print(s[-11: -6])

# (b) the fourth to eighth characters of s inclusive, i.e. "en Ar"
print(s[3:7+1])

# (c) the last five characters of s, i.e. "Arrow"
print(s[6:]) # start from 6 to the end(included) step: 1

# (d) every third character of s from the second character
# onwards, i.e. "rnrw"
print(s[1::3])


# (e) the last five characters of s in reverse, i.e. "worrA".
print(s[10:5:-1])
print(s[-1: -(1+5): -1])

