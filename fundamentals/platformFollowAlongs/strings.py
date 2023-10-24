# in python we use strings for browser urls and text
# the feature we focused on is STRING INTERPOLATION -- F STRINGS
print('this is a sample string')



name = "Zen"
print("My name is", name)

name2 = "Frankie"
print("My name is " + name2)

num = 1
print("my Name is ", num)
# we cannot concatenate a string with an non string variable name
# num = 1
# print("My Name is " + num )

## this is how we would solve this problem
# this line still errors print("Hello " + 42)
## if we convert 42 to a string this will work
print("Hello " + str(42))

## this does the inverse // we take the string and convert it to a int
total = 35
user_val = "26"
# total = total + user_val // this line will error cuz user_val is string//
total = total + int(user_val)
print(total)

# this demonstrates a F-STRING
firstName = "Fab"
lastName = "Ulous"
age = 25
print(f"My name is {firstName} {lastName} and I am {age} years old.")

# before F-STRINGS we used .format()
firstName1 = "Justin"
lastName1 = "Credible"
age1 = 28
print("My name is {} {} and I am {} years old".format(firstName1, lastName1, age1))

# before .format() -- We USED % ... %s for strings ... %d for number
# notice that the %s and %d go in the quotes
hw = "Hello %s" % "world"
print(hw)
py = "I love Python %d" % 3
print(hw, py)

# this is gross . please no
nameTest = "Mario"
ageTest = 35
print("My Name is %s ,I am %d years old." % (nameTest,ageTest))

b = "hello world"
print(b.title())