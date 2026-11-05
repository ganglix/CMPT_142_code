# lists and tuples

# create a list
alist = list(range(10))
print(alist)

empty_list = []
name_list = [
    "Afan", "Janet", "Kelei",
    "Lilith", "Chaz", "Dominick", "Gang",
]
print(name_list)
# indexing and slicing, same as string, or other sequences
print(name_list[0])
print(name_list[-1])
print(name_list[:3])  # first three names


# methods
# add an item: .append(), .extend(), +
name_list.append('Musk')
print(name_list)
name_list.remove('Musk')
name_list.extend(['Musk', 'Zackerberg'])
print(name_list)
new_list = name_list + ['someone']
print(new_list)

# remove an item: .remove(), .pop(), del
new_list.remove('someone')   # removing by value
new_list.pop()   # by default remove the last item .pop(-1), removing by index
del new_list[-1]
print(new_list)


# locating an item: index()
ind = name_list.index('Gang')
name_list.pop(ind)
print(name_list)

name_list.sort()
print(name_list)

# sorting: .sort()





# let do an attempt to use .sort() without changing the old L
alphabets = ['b', 'c', 'a', 'd']
alphabets2 = alphabets   # we have ['b', 'c', 'a', 'd'] in memory, and we give two names to it, like two sticky notes on the [] bucket
alphabets2.sort()

print("alphabets2: ", alphabets2)
print("alphabets: ", alphabets)

# assign a new name does not create a new list,

# # only clone or copy creates a new list with equal values
new_list_alphabets = alphabets.copy()
new_list_alphabets.sort(reverse=True)
print("new_list_alphabets: ", new_list_alphabets)
print('alphabets', alphabets)

# list is mutable ! more examples in flowtrace observations





