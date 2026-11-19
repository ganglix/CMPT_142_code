def is_valid_username(username):
    """
    determines if username meets these constraints:
    - 1-18 characters long
    - can be letters and/or numbers
    - underscore is allowed if it’s not the first character
    username: string to check validity of
    return: True if username satisfies constraints
    """

# Testing - black box
# black box reason: To test if the function does it has promised to do, in the docstring
# coverage: all functionalities stated in the docstring

# test cases
"""
    - 1-18 characters long
inputs: 'a'
outputs_expected: True  #we read the whole docstring to figure out
reason: 'a' is one character long letter, no special chars, no underscore

inputs: ''
outputs_expected: False
reason: '' has the length of 0, not valid, should return False

inputs: 'a' * 18
outputs_expected: True
reason: 'a' * 18 has a length of 18, still with in the length boundaries

inputs: 'a' * 19
outputs_expected: False
reason: 'a' * 19 has a length of 19, exceeding max length


    - can be letters and/or numbers
inputs: '12'
outputs_expected: True  #we read the whole docstring to figure out
reason: only numbers, valid

inputs: '12abc'
outputs_expected: True  #we read the whole docstring to figure out
reason: both letters and numbers, valid

inputs: 'short@gmail.com'
outputs_expected: False  #we read the whole docstring to figure out
reason: it has special characters, not just numbers or letters, and not exceeding max length

    - underscore is allowed if it’s not the first character
inputs: '_underscore'
outputs_expected: False  #we read the whole docstring to figure out
reason: _ is the first character, invalid

inputs: 'a_b'
outputs_expected: True  #we read the whole docstring to figure out
reason: _ is in the middle, valid

inputs: 'a__'
outputs_expected: True  #we read the whole docstring to figure out
reason: _ is not the first character, valid
"""




# test driver example
# test driver is a program that runs the test cases

inputs = 'a'
outputs_expected = True  #we read the whole docstring to figure out
reason = "'a' is one character long letter, no special chars, no underscore"

outputs = is_valid_username(inputs)
# no news is good news
if outputs != outputs_expected:
    print('test case failed')
    print('inputs: ', inputs)
    print('outputs_expected: ', outputs_expected)
    print('function outputs: ', outputs)
    print('reason', reason)




# ~~~~~~~~~~~~~~~~after dictionary~~~~~~~~~~~~~~~~~~~~

# dictionary of test case suite to feed into test driver loop
test_suite = [
    # call for length -zero username (empty string)
    {"inputs": [""],
     "outputs_expected": False,
     "reason": "length must be be 1-18 characters"},

    # call for length -one username of invalid character
    {"inputs": ["+"],
     "outputs_expected": False,
     "reason": "username can only contain letters , numbers , underscores"},

    # call for length -one username of a letter
    {"inputs": ["a"],
     "outputs_expected": True,
     "reason": "username is allowed to have letters"},

    # call for length -18 username of numbers only with trailing underscore
    {"inputs": ["0" * 17 + "_"],
     "outputs_expected": True,
     "reason": "username is allowed to have numbers and trailing underscore"},

    # call for length -three username with letter , number , underscore
    {"inputs": ["a_0"],
     "outputs_expected": True,
     "reason": "username is allowed to have letters , numbers , underscore"},

    # call for length -three username with letter , number , starting underscore
    {"inputs": ["_a0"],
     "outputs_expected": False,
     "reason": "can’t start with underscore"},

    # call for length -18+ username of letters and numbers
    {"inputs": ["a0" * 18],
     "outputs_expected": False,
     "reason": "can’t have more than 18 characters"}
]

# a generic loop for test drivers
# the inputs are in a list , so it has to be modified
for test in test_suite:
    inputs = test["inputs"]
    result = is_valid_username(inputs[0])

    if result != test["outputs_expected"]:
        print("Testing fault: is_valid_username () returned", result, "on inputs", inputs,
              "test reason:", test['reason'])
