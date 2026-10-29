# This demonstration shows you how to call methods on string objects.


# initialize some variables to play with
url = 'www.engineering.usask.ca'

# find the location of the first period in the url
idx = url.find('.')   # .find() will return the index of first period
print(idx)

# count the number of periods in the url
print(url.count('.'))



#----------------------------------------
s = ' CMPT 142 '
# remove white space
print(s.lstrip()) # by default remove white space from the left
print(s.rstrip()) # remove white space from the right
print(s.strip())  # remove white space from both ends

# remove all spaces?
print(s.replace(' ',''))  # repace space string with empty string


# ------------------------
# count the number of characters in the url after removing "www."
short_url = url.replace("www.","")
print(short_url)
print( len( short_url ) )



# useful in practice?

# e.g. ask user to type y/n

# user_type = input('please type y/n').lower() # user input will be turned to lower case anyways


# strings are immutable, all these methods create a copy


# how do I know what kind of methods are out there? How do I know the syntax/usage?

# for name in dir(url):
#     print(name)