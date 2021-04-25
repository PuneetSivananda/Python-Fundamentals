our_dictionary = {"key1":"value1",
"key2":"value2"}

person = {"name":"John doe", 
"height":"7'5",
"location":"Memphis"}

print(our_dictionary)

print(person)
print(person["name"])
print(person["height"])

person["eye_color"] = "blue"
print(person)

person.pop("eye_color")
print(person)