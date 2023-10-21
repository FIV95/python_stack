
#primitive types

is_hungry = True
has_freckles = False

age = 35
weight = 160.57
name ="Joe Blue"

# composite types

# The following is a tuple:
# These cannot be modified after their creation // can also hold a mix of data
dog = ('Bruce', 'cocker spaniel', 19, False, ['weight: 20'])
print(dog[0])
# dog[1] = 'dachshund' # this will not work because we cannot reassign items within the tuple after its creation
print(dog[4])
d = dog[4]
print(d)
print(dog) ## notice that in this tuple even though I grab data from it and store that as variable it remains in the tuple

# The following is a list:
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])
ninjas[0] = 'Francis'
print(ninjas)
ninjas.append('Michael')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)

# the following is a dictionary:
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack' # we reassigned new_person's name to be Jack
new_person['operating_system'] = 'Mac'
print(new_person)
print(new_person['has_glasses']) ## this line finds the key has_glasses and outputs the value in that key for new_person
new_person['hobbies'] =  ['climbing', 'coding']
print(new_person['hobbies'][0]) ## this line finds hobbies 'the key' of new_person and prints the 0th index
w = new_person.pop('weight') ## for some reason this removes weight from my dictionary
print(new_person)
print(w)

print(type(2.63)) ## should output that this is a float
print(type(new_person)) ## should output that this is a dict
print(len(new_person))
print(len('Coding Dojo')) ## length does count whitespace so this should be 11
print(len('CodingDojo')) ## testing if whitespace is counted toward length count - this is TRUE 10