person = {
      "first": "Ada",
      "last": "Lovelace",
      "age": 42,
      "is organ donor": True,
      "favorite color": "Red"
      }
capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print(capitals)

print(person["first"])
person["Middle Name"] = "Wong"
print(person)

# person["email"] = "alovelace@codingdojo,com"
print(person)

# if key not in dictionary: THIS IS HOW WE CHECK
if "email" not in "person":
      person["email"] = "alovelace@codingdojo,com"
print(person["email"])

person["last"] = "Boba"
print(person)

if "favorite color" not in person:
      person["favorite color"] = "Blue"
else:
      print('Are you trying to replace the favorite color?')

print(person)

full_name = person["first"] + " " + person["Middle Name"] + " " + person["last"]
print(full_name)

removed_value = person.pop("favorite color")
del person["is organ donor"]
print(person)

# length shows how many keys there are.
print(len(person))
#prints the dictionary as a string
print(str(person))
#prints the type
print(type(person))

# clear() removes all elements from a dictionary
#<dictionaryName>.get(<keyname>,default=None)
print(person.get('income', None))
person.update({'first': 'Leon'})
print(person['first'])

my_dict = {
      "name": "Noelle",
      "language": "Swedish"
}
for each_key in my_dict:
      print(each_key)

# OR TO GET EACH VALUE
for each_value in my_dict:
      print(my_dict[each_value])

capitals = {
      "Washington": "Olympia",
      "California": "Sacramento",
      "Georgia": "Atlanta",
      "New Mexico": "Santa-Fe",
      "Nevada": "Carson City",
      "New York": "Albany"
}
for key in capitals.keys():
      print(key)

for values in capitals.values():
      print(values)

for key, val in capitals.items():
      print(key, " = ", val)