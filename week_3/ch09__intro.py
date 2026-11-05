# Control Flow: Repetition
# what is a computer good at?
# repeat till what? when?

# while loop starts and stops according to a condition
## things I want to mention: condition boolean, if/while

# counting example : 1~5
# count = 0
# while count < 5:
#     count = count + 1
#     print(count)

count = 1
while count <= 5:
    print(count)
    count = count + 1

print('after the while loop, count =', count)




# for : repeat over a sequence
# mention types of sequence: string, range, list, dict

s = 'cmpt142'
# for i in range(0,10):
#     print(i)   # print 0, 1, 2... 9
print('~'*20)

for i in range(len(s)):   #  0, 1, 2...len(s)-1
    print(s[i], end=' ')
print()

for char in s:   # 'c', 'm', 'p'... '2'
    # char is a good variable name and that is what we are iterating over s
    print(char)

