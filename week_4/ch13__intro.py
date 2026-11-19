# dictionary {key : value, key1 : value1}, Those records or pairs are not ordered

# KEYS

# VALUES

phone_book = {'Gang': '3068888888', 'Janet': 3060000001}
print(phone_book)
print(phone_book['Gang'])

# what type of data can be a dictionary key
# any immutables can be the key: int, string, float, tuple
# mutables can NOT be the key: list, dict

# add record
phone_book['Dominic'] = '3061111111'
print(phone_book)
# remove record
phone_book.pop('Gang')
print(phone_book)

# look-up
for name in phone_book:   # {name: phone number}
    print(phone_book[name])

# print(phone_book['Gang'])   # Keyerror, 'Gang' is not there

# how to avoid keyerror, when we are not sure if the key exists
if 'Gang' in phone_book:
    print('Gang:', phone_book["Gang"])
else:
    print("Gang not found")

# .get(a,b) meaning try to get dict[a], if a is not a key (do not break), then return b
print(phone_book.get('Gang','message: Gang not found'))

# value can also be a dict

contact = {}
contact['Chaz'] = {'phone': '+1 555 555 555', 'email': 'vip@usask.ca'}
print(contact)
contact['others phone'] = phone_book
print(contact)

from pprint import pprint
pprint(contact)

# When work with dict, always be clear: what is the key, what is the value!!