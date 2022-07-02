num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True #variable declaration, initializing boolean
string = 'Hello World' #variable declaration, initializing string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initializing list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initializing dictionary 
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initializing tuple
print(type(fruit)) # log statement, type check, list 
print(pizza_toppings[1]) # log statement, list, access value
pizza_toppings.append('Mushrooms') # list, add value
print(person['name']) # log statement, list, access value
person['name'] = 'George' # dictionary, access value, change value
person['eye_color'] = 'blue' # dictionary, add value
print(fruit[2]) # log statement, tuples access value

if num1 > 45: # conditional, if
    print("It's greater") # log statement, string
else: # conditional, else
    print("It's lower") # log statement, string

if len(string) < 5: # conditional, if, length check
    print("It's a short word!") # log statement, string
elif len(string) > 15: # conditional, length check
    print("It's a long word!") # log statement, string
else: # conditional, else
    print("Just right!") # log statement, string

for x in range(5): # for loop, variable declaration, end
    print(x) # log statement, 
for x in range(2,5): # for loop, variable declaration, start, end
    print(x) # log statement
for x in range(2,10,3): # for loop, variable declaration, stat, stop, increment
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # while loop, stop
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() # list, delete value
pizza_toppings.pop(1) # list , delete value

print(person) # log statment, dictionary
person.pop('eye_color') # dictionary, delete value
print(person) # log statment, dictionary

for topping in pizza_toppings: # for loop, variable declaration
    if topping == 'Pepperoni': # conditional if, 
        continue # continue
    print('After 1st if statement') # log statement, string
    if topping == 'Olives': # conditional if 
        break # break

def print_hello_ten_times(): # function declaration
    for num in range(10): # for, variable declaration, end
        print('Hello') # log statement, string

print_hello_ten_times() # function call

def print_hello_x_times(x): # function declaration, parameter
    for num in range(x): # for loop, variable declaraction, end
        print('Hello') # log statement, string

print_hello_x_times(4) # function call, arugument

def print_hello_x_or_ten_times(x = 10): # function declaration, parameter
    for num in range(x): # for loop, variable declaration, end
        print('Hello') # log statement, string

print_hello_x_or_ten_times() # function call
print_hello_x_or_ten_times(4) # function call, argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
