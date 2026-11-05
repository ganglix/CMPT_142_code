# Write a Python function that uses a for-loop to print the
# number of times each lowercase vowel (a,e,i,o,u) occurs in a
# string s. e.g. "piece" prints "a:0 e:2 i:1 o:0 u:0".

s = "piece"

# keep tracking of 'e'
# count = 0
# for char in s:
#     if char == "e":
#         count += 1
# print(f'e:{count}')

# keep tracking of 'a e i o u'
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for char in s:
    if char == "a":
        count_a += 1
    elif char == "e":
        count_e += 1
    elif char == "i":
        count_i += 1
    elif char == "o":
        count_o += 1
    elif char == "u":
        count_u += 1
print(f'a:{count_a} e:{count_e} i:{count_i} o:{count_o} u:{count_u}')