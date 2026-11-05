# while vs. for
# In this demonstration, we’ll see a situation where using a
# while-loop is preferable to using a for-loop.

# password example

# correct password
passcode = "cmpt142"
count_max = 3
# ask user to type a password for the first time
user_input = input("Please enter your password: ")
count = 1

# keep asking until the user gets the correct password or exceed max trials
while user_input != passcode and count < count_max:
    user_input = input("Password is not correct, please enter your password again: ")
    count += 1   # same as count = count + 1

# at this point, the while loop is completed/stopped
#  user_input != passcode and count < count_max is False

# two outcomes
# either: the user gets the correct passward
if user_input == passcode:
    print("password is correct", count, 'attempt(s) made')
else:
    # or: count < count_max is False, count reaching the max
    print("password is wrong", 'max attempt(s)', count_max ,'made')
