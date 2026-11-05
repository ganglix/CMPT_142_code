# Write Python code which asks a user to input a string from
# the console until it is identical to pre-defined string passcode.
# When this occurs, print the number of attempts made to
# enter the correct string. e.g. "3 attempt(s) made."

# correct password
passcode = "cmpt142"

# ask user to type a password for the first time
user_input = input("Please enter your password: ")
count = 1

# keep asking until the user gets the correct password
while user_input != passcode:
    user_input = input("Password is not correct, please enter your password again: ")
    count += 1   # same as count = count + 1

# at this point, the while loop is completed/stopped
# only because user_input != passcode is False, the user did get the correct password
print("password is correct", count, 'attempt(s) made')
