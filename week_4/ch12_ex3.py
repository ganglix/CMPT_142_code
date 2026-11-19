def is_valid_password(password):
    """
    determines if password meets these constraints:
    - 9-18 characters long
    - no Underscores or minus _,-
    password: string to check validity of
    return: True if password satisfies constraints
    """
    is_valid = True

    if len(password) < 9 or len(password) > 18:
        is_valid = False
        return is_valid
    if "_" in password:
        is_valid = False
        return is_valid
    if "-" in password:
        is_valid = False
        return is_valid

    return is_valid


# Testing - white box
# reasoning: Read the code, strategically pick the test cases that cover every single line of code.
# make sure to trigger all branches (if-elif-else), also for while-loop (no loop at all, when while-condition is false, repeat once, or many times, or check if it is inf loop)

"""
# Test cases that triggers every single line of code

inputs: '123456'
outputs_expected: False  # Do not use code to find this expected output, because we are testing the code, and we do not
                         # trust the code at all. We determined the expected output by reading the docstring!
                         
reason: line 11, the input is shorter than 9, which triggers if-statement to be true, so the block of code under that if-statement is executed


inputs: '_'+'a'*10
outputs_expected: False  # Do not use code to find this expected output, because we are testing the code, and we do not
                         # trust the code at all. We determined the expected output by reading the docstring!
                         
reason: line 14, the input has _ and satisfies length constrains, which triggers line 14 if-statement to be true, so the block of code under that if-statement is executed

inputs: '-'+'a'*10
outputs_expected: False  # Do not use code to find this expected output, because we are testing the code, and we do not
                         # trust the code at all. We determined the expected output by reading the docstring!
                         
reason: line 17, the input has - and satisfies length constrains, which triggers line 14 if-statement to be true, so the block of code under that if-statement is executed



# to really have full coverage of code, we still need to test line 21

inputs: '[sddeptf123'
outputs_expected: True
reson: a valid password to skip all if-statements and check line 21
"""

# test drivers has same structure as black-boxing testing
inputs = '-'+'a'*10
outputs_expected = False  # Do not use code to find this expected output, because we are testing the code, and we do not
                         # trust the code at all. We determined the expected output by reading the docstring!
reason = "line 17, the input has - and satisfies length constrains, which triggers line 14 if-statement to be true, so the block of code under that if-statement is executed"

outputs = is_valid_password(inputs)
if outputs != outputs_expected:
    print("Test failed")
    print('inputs: ', inputs)
    print('outputs_expected: ', outputs_expected)
    print('function returns: ', outputs)
    print('reason: ', reason)
