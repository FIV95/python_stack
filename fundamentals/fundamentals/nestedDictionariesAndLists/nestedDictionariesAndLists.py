x = [ [5,2,3], [10,8,9] ]
students = [
      {"First Name": 'Michael', "Last Name": 'Jordan'},
      {"First Name": 'John', "Last Name": 'Rosales'}
]
sports_directory = {
      "Basketball":  ['Kobe', 'Jordan', 'James', 'Curry'],
      "Soccer": ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {"x": 10, "y": 20} ]

#step number 1
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]  = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["Last Name"] = "Bryant"
print(students[0]["Last Name"])

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['Soccer'][0] = 'Andres'
print(sports_directory['Soccer'][0])
# Change the value 20 in z to 30
z[0]["y"] = 30
print(z[0]["y"])

# def interateDictionary(list):
#       for dictionaries in list:
#             print(dictionaries)
#             for key, value in dictionaries.items():
#                   print(f"{key} = {value}, ")

# interateDictionary(students)

def interateDictionary(list):
      for dictionary in list:
            for key in dictionary:
                  print(f'{key}- {dictionary[key]}')

interateDictionary(students)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

## I really dont understand why this works...
def iterateDictionary(listElement):
      for dictionary in listElement:
            output = ''
            for key, value in dictionary.items():
                  output += (f'{key} - {value}, ')
            output = output.rstrip(', ')
            print(output)

iterateDictionary(students)




#i dont know whats going on here - This creates a list out of the keys and values but this strategy got me no where.

# def key_list_creation(listElement):
#       key_list = []
#       for dictionary in listElement:
#             for key in dictionary.keys():
#                   key_list.append(key)
#       print(key_list)
#       return key_list

# key_list_creation(students)

# def value_list_creation(listElement):
#       value_list = []
#       for dictionary in listElement:
#             for value in dictionary.values():
#                   value_list.append(value)
#       print(value_list)
#       return value_list


# key_list_creation(students)
# value_list_creation(students)

# def iterateDictionary(listElement):
#       for dictionary in listElement:
#             key_list_creation(listElement)
#             value_list_creation(listElement)
#             key_list = []
#             value_list = []
#             print(f'{key_list[0]}  {value_list[0]}')

# print(iterateDictionary(students))

students2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name,some_list):
      for dictionary in some_list:
            print(dictionary[key_name])
            for key in dictionary:
                  # if key != [key_name]: I have no clue what i was doing here either.
                  #       continue
                  # print(dictionary[key_name])
                  pass

print(iterateDictionary2('first_name',students2))
print(iterateDictionary2('last_name',students))

dojo = {
      'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
      'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Hinh', 'Devon']
}
# def dictionaryStatFinder(dictionary):
#       list_count = 0
#       key_list_length = 0
#       value_list_length = 0
#       key_list = []
#       value_list = []
#       for listnumber in dictionary:
#             list_count += 1
#             if listnumber == 0:
#                   list_count = 'There was only one list inside this dictionary'
#             for keys in dictionary.keys():
#                   key_list.append(keys)
#             key_list_length = len(key_list)
#       for values in dictionary.values():
#             value_list.append(values)
#             value_list_length = len(value_list)
#             print(f'There are {list_count} lists in the dictionary')
#             print(f'{value_list} has {value_list_length} entries')
#             print(f'{key_list} has {key_list_length} entries')

# print(dictionaryStatFinder(dojo))

# def dictionaryStatTracker(dictionary):
#       for listelement in dictionary:
#             keyName = dictionary[]

dojo = {
      'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
      'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Hinh', 'Devon']
}

#function needs to:
#For each key
# prints out each Key capitalized along with list length
#proceeding each item in the respecitve value


def dictionaryStat(dictionary):
      for key in dictionary.keys():
            list = dictionary[key]
            length_of_list = len(list)
            print(f'{length_of_list} {key.title()}')
            for item in list:
                  print(item)


dictionaryStat(dojo)