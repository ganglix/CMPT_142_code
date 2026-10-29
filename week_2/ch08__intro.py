# control flow - branching
if CONDITION:
    # DO THIS BLOCK if CONDITION is true
    #####SOMETHING#######
else:
    # instead do this block if CONDITION is false

# eventually run the main code
# Do something after the if-else block

if CONDITION1:
    #  do something
else:
    if CONDITION2:
        # if the condition2 is true
        # do this block
    else:
        # if the condition2 is false


if CONDITION1:
    #  do something
elif CONDITION2:
    # if the condition2 is true
    # do this block
else:
    # if the condition2 is false

# Relational and Boolean operator, data type
# relational > < == !=

2 > 3 # this expression return False, a bool value

# Things that can produce a boolean value
"Canada !!!".isalnum()  # check if the string contains only alphabet and number


# Boolean operator
# not and or

# precedence: do not first, then and  then or
# not > and > or   "nao"   always do () first


food = True
drink = True
print(not food or drink)