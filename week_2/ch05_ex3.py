# Given variables:
nation = "Canada !!!"
nation_motto = "From Sea to Sea"

# Write expressions to:
# (a) Determine if nation has only alphabetic letters and digits
print(nation.isalnum())

# (b) Remove "!" characters and whitespace from nation
print(nation.replace(" !!!", ""))
print(nation.strip("! "))   # "! " tells .strip() to remove ! and space (! and space are garbage to be removed)

# (c) Find the location of the first "Sea" substring in nation_motto
print(nation_motto.find('Sea'))

# # step 1 find the first Sea
# idx_1st = nation_motto.find('Sea')
#
# # step 2 slice off the first Sea
# short = nation_motto[idx_1st + 1 :]
# print(short)
#
# # step 3 find the Sea in short
# idx_2nd_in_short = short.find("Sea")
#
# # step 4 add idx_2nd to idx_1st
#
# print(idx_2nd_in_short + idx_1st)   # 1 off, wrong


# to use slice parameter directly inside .find() so the orignial indexing is not change

print(nation_motto.find('Sea', nation_motto.find('Sea')+1))   # +1, start fing the next index after first Sea

