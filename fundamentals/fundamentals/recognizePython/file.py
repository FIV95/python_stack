num1 = 42 #variable declaration , Data Types integer
num2 = 2.3 #variable declaration  Data Types Float
boolean = True# variable delcaration Boolean
string = 'Hello World' #variable declaration, Data Type, String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration - list full of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #initilize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #initilize tuple
print(type(fruit))  #log statement for a type check on fruit - should return tuple
print(pizza_toppings[1]) # log statement for index 1 of the pizza_topping list - should return Sausage
pizza_toppings.append('Mushrooms') # appends the string mushrooms to the end of the pizza_toppings list
print(person['name']) # log command - looks in the dictionary called person and grabs their name. should print John
person['name'] = 'George' # changes the key-value name in the person dictionary to John
person['eye_color'] = 'blue' #  eye_color is not a key inside of person so this line will create it and add it to the dictionary
print(fruit[2]) # prints the 2nd index of the list titled fruits

if num1 > 45: #initializes a conditional IF statement - 42 > 45  FALSE
    print("It's greater") #print statement if conditional TRUE
else: ## else Statement
    print("It's lower") #print statement if conditional FALSE

if len(string) < 5: # if thje length of string is less than 5 // current length of string is = 11 // 11 < 5 FALSE
    print("It's a short word!") # print statement for conditional TRUE
elif len(string) > 15: # creates an else if statement to then check if 11 > 15 TRUE
    print("It's a long word!") #print statement for condtitional  THIS WOULD be OUTPUT
else:
    print("Just right!") # if string not less than 5 or NOT greater than 15 - this command prints Just Right

for x in range(5):  #this is a for loop . 5 is our stopping point . x will become 1,2,3,4, and will print each step. this is not inclusive (5)
    print(x) # this prints out each step in our loop
for x in range(2,5): #this is another for loop this will start at 2 and will print 2,3,4. // again this is not inclusive to (5)
    print(x) # this prints out each step in our loop
for x in range(2,10,3): #this is another for loop // this loop will increment by 3 each time it passes . the stopping point for this loop is 10
    print(x) # this should output 3,5,8
x = 0 # declares a variable x and x holds the value 0
while(x < 5): #this is a while loop // #while 0<5 --- x increments +1 ///
    print(x) # log statement of the value x
    x += 1 # itterates on x by +1  this will still be not inclusive for (5)

pizza_toppings.pop() #this accesses the list pizza_toppings and pops the last value
pizza_toppings.pop(1) # this access the list pizza_toppings and pops index1 // this should remove Sausage from the list

print(person) # this prints the whole dictionary of person
person.pop('eye_color') # this accesses the person dictionary and pops the eye_color key from the dictionary
print(person) #having the previous line remove the eye color key from the dictionary this log statement should print the dictionary without the key and its value for eyecolor

for topping in pizza_toppings: #were making a for loop here // for each index within the pizza_toppings list
    if topping == 'Pepperoni': #if that topping is Pepperoni
        continue # the loop continues
    print('After 1st if statement') #this line logs a string that says 'After 1st if Statement'
    if topping == 'Olives': #the loop continues printing but it checks if topping is olives and if so
        break # the loop breaks and stops

def print_hello_ten_times(): # this line declares a function // this function takes in no parameters
    for num in range(10): #this function contains a for loop and searches for the numbers between 0 and 10
        print('Hello') #this command logs each time a number is found between 0 and 10

print_hello_ten_times() # this actually executes the function called print_hello_ten_times

def print_hello_x_times(x): #this line declares the same function as before but wants us to pass one parameter to the function
    for num in range(x): # for each number between 0 and our parameter x
        print('Hello') # console log "Hello"

print_hello_x_times(4)  # this invokes the function from line 59 and passes 4 as the arguement.. # this should print Hello four times

def print_hello_x_or_ten_times(x = 10): # this function is telling us the exact parameter/arguement it wants passed through it by default upon execution
    for num in range(x): # for each number between 0 and 10
        print('Hello') # print hello for each number found

print_hello_x_or_ten_times() # this function call uses the default value of 10
print_hello_x_or_ten_times(4)# this function replaces the default parameter value to 4


"""
Bonus section
"""

# print(num3) #NameError name <variable Name> is not defined
# num3 = 72  # declares variable num3 and assigns it a value of 72
# fruit[0] = 'cranberry' #cannot make adjustments to a tuple #tuple object does not support item assignment
# print(person['favorite_team']) #keyError: 'favorite_team' cannot print command a key the dictionary does not possess
# print(pizza_toppings[7]) #Index Error list index is out of range
#   print(boolean) #unexpected Indent
# fruit.append('raspberry') #cant modify tuples - tuple object has no attribute append
# fruit.pop(1) #cant modify tuples tuple object has no attribute pop