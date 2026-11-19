# Exercise 2

# Suppose we have dictionary availability:
# keys: friend’s name
# values: list of days they are available to play a game
# (a) Write a function that accepts an availability dictionary and returns a new dictionary mapping days to
# friends who can play that day.
# (b) Using the function from a):
# Find the day most friends can attend to play the game
# List who can and can not attend the session that day

availability = {"Neo":      ["Monday"],
                "Morpheus": ["Sunday"],
                "Smith":    ["Monday", "Tuesday"]}

def scheduler(availability):
    """
    Convert a dictionary of availability to a dictionary of schedule
    :param availability: dict, {name: list of available days}
    :return: dict, {day: list of available names}
    """
    # initiate schedule {}
    schedule = {}  #day: list of available names

    # chech every entry in availability
    for name in availability:
        day_list = availability[name]
        for day in day_list:
            # if the day is not in the schedule yet, initialize it
            if day not in schedule:
                schedule[day] = []
        # then append that name to the existing day
            schedule[day].append(name)   # schedule[day] is the list of names
    return schedule

print(scheduler(availability))

# find the day that most friends can attend



# List who can and can not attend the session that day

