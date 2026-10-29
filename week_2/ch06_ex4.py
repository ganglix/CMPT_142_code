# Flowtrace with function

# status = "Healthy"
# def set_status(s):
#     status = s
#
# set_status("Poisoned")
# print(status)

"""
status = "Healthy"
set_status("Poisoned")
---------another piece of paper, under the hood of the function--------
    s = "Poisoned"
    status = "Poisoned"
----------------------end of the function--------------------

print("Healthy")
"""

status = "Healthy"
def set_status(s):
    return s

status = set_status("Poisoned")
print(status)





#~~(things I want to mention: scope, return, dangerous thing to do)






# optional: global var can be accessed from inside the func but can not be assigned
