s = 'fire'
L = [1, 2, 3]
L2 = [ [1 , 2] , [3 , 4] ]
print(
s + "water",
    '\n',
# (b)
L + [4, 5, 6],
    '\n',

    # (c)
# L + s,   # error
L + [s],
    '\n',

    # (d)
L + L2,
    '\n',

    # (e)
L*3,
    '\n',

    # (f)
"f" not in s,
    '\n',

    # (g)
"fr" in s,
    '\n',

    # (h)
1 in L2,
    '\n',

    1 in L2[0] #L2's first sublist

)