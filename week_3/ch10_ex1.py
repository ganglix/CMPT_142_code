# A given list called pkg_weights contains weights of parcels
# (in lbs) queued for shipping. Write Python code that:
# (a) Creates list light_pkgs of parcels that weigh less than 5
# lbs from pkg_weights
# (b) Removes parcels from pkg_weights that exceed 15 lbs
# (c) Print the:
# • contents of light_pkgs in ascending order
# • number of parcels in light_pkgs
# • number of parcels removed from pkg_weights

pkg_weights = [2, 6, 8, 34, 56, 67, 4, 2, 33]

# (a) Creates list light_pkgs of parcels that weigh less than 5
light_pkgs = []
for weight in pkg_weights:
    if weight < 5:
        light_pkgs.append(weight)
print(light_pkgs)

# (b) Removes parcels from pkg_weights that exceed 15 lbs
# for weight in pkg_weights:  # Never iterate over a size-changing list
#     if weight > 15:
#         pkg_weights.remove(weight)
# print(pkg_weights)

# solution 1: use a clone of the list to iterate over
# for weight in pkg_weights.copy():  # .copy() is seperate new list idential to the original
#     if weight > 15:
#         pkg_weights.remove(weight) # the clone/copy did not change
# print(pkg_weights)

# solution 2:
heavy_pkgs = []
for weight in pkg_weights:
    if weight > 15:
        heavy_pkgs.append(weight)

for weight in heavy_pkgs:
    pkg_weights.remove(weight)
print(pkg_weights)

# (c) Print the:
# • contents of light_pkgs in ascending order

# light_pkgs.sort()
# print(light_pkgs)
# without changing light_pkgs
print(sorted(light_pkgs))  # sorted() is function that creates a SORTED NEW list


# • number of parcels in light_pkgs
print("number of parcels in light_pkgs: ", len(light_pkgs))


# • number of parcels removed from pkg_weights














# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~things I want to mention
# Modifying list while iterating DO NOT DO IT
# don't change list if possible
# use a clone





