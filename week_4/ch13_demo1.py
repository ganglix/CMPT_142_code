# demo1
# Tower Name Location
# Tokyo Skytree Japan
# Canton Tower China
# CN Tower Canada

tower = {
    "Tokyo Skytree": "Japan",
    "CN Tower": "Canada",
    "Canton Tower": "China",
}

# Let’s modify the dictionary:
# (a) Remove the entry whose location is "Canada"
for tower_name in tower.copy():
    if tower[tower_name] == "Canada":
        tower.pop(tower_name)
print(tower)

# (b) Add a new entry with tower name "Eiffel Tower" and
# location "Paris"
tower['Eiffel Tower'] = "Paris"

# (c) Oops! Update the tower entry "Eiffel Tower" to have
# location "France"

tower['Eiffel Tower'] = "France"



