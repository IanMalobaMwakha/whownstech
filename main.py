# PYTHON REVISION

"""
has_high_income = True
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print("Eligible")

temp = 35
if temp > 30:
    print("Its a hot day")
elif temp < 10:
    print("its a cold day")
elif temp != 35:
    print("hgfddfghj")



weight = input('Weight: ')
units = input('L(bs) or K(gs): ')
if units.upper() == "L":
    converted_weight = int(weight) * 0.4
    print(f'Your weight is {converted_weight} kilograms')
else:
    converted_weight = int(weight) / 0.4
    print(f'Your weight is {converted_weight} pounds')

    i = 1
while i <= 5:
    print(i * "*")
    i += 1

secret_number = 9
guess_count = 0
max_count = 3
while guess_count < max_count:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!!")
        break
else:
    print("You lost, sorry..")


command = ""
started = False
while command.lower() != "quit":
    command = input(">: ").lower()
    if command == "start":
        if started:
            print("THE CAR IS ALREADY STARTED!!!")
        else:
            started = True
            print("The car has started...")
    elif command == "stop":
        if not started:
            print("THE CAR IS ALREADY STOPPED!!!")
        else:
            started = False
            print("The car has stopped...")
    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == "quit":
        break
    else:
        print("I don't understand that!")

for i in range(3, 15, 3):
    print(i)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total} ksh.")

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2, 2]
for number in numbers:
    Output = ""
    for x_count in range(number):
        Output += "X"
    print(Output)

numbers[0] = 8
print(numbers)

largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)


print("Ian Maloba")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)


def UoPeople():
    print ('You are most welcome  to this great platform, FEEL AT CLASS')
print ('|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|')
user = str(input('Enter your name: '))
print (user + ' the following are the group motives')
print ('''🫵🏼 Helping out each other to archive their expectations at the UoPeople courses.\n
🫵🏼 Reaching out to each other for knowledge & idea sharing about different topics at hand.''')
UoPeople ()
print ('|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|')


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [5, 6, 7]
]
print(matrix[0][0])
matrix[2][2] = 14
print(matrix)
for items in matrix:
    for values in items:
        print(values)

mylist = [2, 4, 5, 6, 9, 9, 5, 7]
mylist.sort()
print(mylist)
print(19 in mylist)

uniques = []
for number in mylist:
    if number not in uniques:
        uniques.append(number)
print(uniques)
 # TUPLES
first_tuple = (1, 2, 3)
#UNPACKING
coordinates = (5, 6, 7)
x, y, z = coordinates
print(x)

print(float(20))


class Converter:
    def number_to_word(phone_number):
        digits_mapping = {
            "1": "One",
            "2": "Two",
            "3": "Three"
        }

        Output = ""
        for values in phone_number:
            Output += digits_mapping.get(values, values) + " "
        return Output

    phone_number = input("ENTER THE NUMBER: ")
    print(number_to_word(phone_number))




class Mammals:
    def reproduce(self):
        print("Its a reproduction")

class Person(Mammals):

    def __init__(self, name):
        self.name = name
    def talk(self):
         print(f"{self.name} is talking")

person1 = Person("Ian")
person1.talk()


import math
import random
from random import randrange

for i in range(1):
    print(random.randrange(0, 17))

myAns = "We Ian by name and we want to be great at coding"
splitAnswer = myAns.split(' ')
myDict = {
    "we": "I",
    "We": "I"
}
Output = ""
for ch in splitAnswer:
    Output += myDict.get(ch, ch) + " "
print(Output)



birth_year = input("What is your birth year? ")
age = 2023 - int(birth_year)
print("You are " + str(age) + " years old.")


# TYPES IN PYTHON
# integer
number = 20
print(type(number))

# string
name = "Anne"
print(type(name))

# boolean
is_old = True
print(type(is_old))

# float
angle = 2.225
print(type(angle))

# Weight Converter

weight_in_pounds = input("What is your weight in pounds? ")
weight_in_kg = int(weight_in_pounds) * 0.4
print("Your weight in kg is " + str(weight_in_kg) + " Kilograms")




# SQUARE BRACKET SYNTAX

course = "Py thon"
print(course[2])


# Formatted Strings
name = "John"
print("You are " + name)
print(f"You are {name}")


# STRING METHODS

# 1.  The len function -> Is used to count the number of characters in a string
course = "Python"
print(len(course))

# Methods
subject = "MAThEmatics"
print(subject.upper())
print(subject.lower())
print(subject.find("E"))

name_of_course = "Python for Beginners"
print(name_of_course.replace("for", "of"))

course = "Python"
number_of_characters = len(course)
print(number_of_characters)

marks = 7
percent = marks/10 * 100
Output = percent
print(Output)


# The in Operator
favourite_subject = "Web Development"
our_answer = "eb" in favourite_subject
print(our_answer)

# Arithmetic/Mathematical Operations
calculation1 = 7 // 3  # double slash -> returns the whole number and ignores the decimal part
print(calculation1)

calculation2 = 7 % 3  # modulus -> used to return the remainder of division
print(calculation2)


name = 'Python for beginners'
print(name[4:])
fname = 'kelvin'
lname = 'Funyui'
print(f"My first name is {fname} and my last name is {lname}")


birthhyr = input("When were you born? ")
age = 2023 - int(birthhyr)
print(f"Age: {age}")


# SQUARE BRACKET SYNTAX

course = "Python"
print(course[:])

name_of_course = "Python for Beginners"
print(name_of_course.replace("Beginners", "Elites"))


# Augmented assignment Operator
x = 10
x = 10 + 3  # increment
print(x)

x = 10
x += 3
print(x)



# Operator precedence
# BODMAS , PEMDAS

y = 12 * 3 + 5 - 12 + (3 - 2) * 4
print(y)



# If statements
is_hot = True
if is_hot:
    print("It is a hot day!")


if its hot
   It is a hot day
   Drink plenty of water
Otherwise if it is a cold day
   It is a cold day
   Wear warm clothes
Otherwise
   It is a lovely day


is_hot = False
is_cold = True
is_warm = False
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")
elif is_warm:
    print("It is a warm day")
elif is_cool:
    prin("It is a cool day")
else:
    print("It is a lovely day")

print("Have a great day!")

EXERCISE
----------------------
Imagine Price of a house is 1M
If a buyer has good credit
        We put down the price by 10% (We give them a downpayment of 10%)
Otherwise a buyer do not have good credit
        We put down the price by 20% (We give them a downpayment of 20%)



price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print("This is the down payment: $" + str(down_payment))
print(f"This is the Down Payment: ${down_payment}")


# LOGICAL OPERATORS

# The logical AND operator -> All conditions are true
has_good_credit = True
has_high_income = True

if has_good_credit and has_high_income:
    print("This customer has good credit and has high income")


# The logical OR operator -> Atleast one condition is true
has_good_credit = True
has_high_income = True

if has_good_credit or has_high_income:
    print("Great")


# The Logical NOT Operator -> Used to convert True boolean to False
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for a loan!")


# COMPARISON OPERATORS
# >, <, <=, >=, ==(Equality operator), !=(Not equal to)

temperature = 11
if temperature >= 30:
    print("It is a hot day")
elif temperature <= 10:
    print("It is a cold day")
else:
    print("It is neither hot nor cold")

# != (NOT EQUAL TO)
age = 81
if age != 80:
    print("You won't get financial support")
else:
    print("You will get financial support")

"""
import math

# WEIGHT CONVERTER

"""
Build a program that will allow the user to enter their weight in either kilograms or pounds
and then convert it in the other unit
Example;
Weight: 160
Is this value L(bs) or K(gs): L
You are 72.0 kilos


weight = input("Weight? ")

unit = input("Is this L(bs) or K(gs)? ")

if unit.upper() == "L":
    converted_weight = int(weight) * 0.45
    print(f"You are {converted_weight} kilos.")

else:
    converted_weight = int(weight) / 0.45
    print(f"You are {converted_weight} pounds.")




weight = input("Enter your Weight ")
unit = input("Is the unit in L(bs) or K(gs) ")

if unit.upper() == "L":
    weight_in_kilos = float(weight) * 0.4
    print(f"Your weight in Kilograms is {weight_in_kilos} kgs.")

else:
    weight_in_pounds = float(weight) / 0.4
    print(f"Your weight in pounds is {weight_in_pounds} lbs.")


Build a program that will allow the user to enter their weight in either kilograms or pounds
and then convert it in the other unit
Example;
Weight: 160
Is this value L(bs) or K(gs): L
You are 72.0 kilos



# Logical Operators AND , OR, NOT

has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")


# Comparison Operators <,>, <=, >=, !=

temperature = 30

if temperature != 30:
    print("It is  a hot day")
elif temperature < 10:
    print("It is a cold day")
else:
    print("It is neither hot nor cold")



weight = input("Weight: ")
unit = input("Is the unit you entered above K(gs) or L(bs): ")
if unit == "L":
    weight_in_kgs = int(weight) * 0.45
    print("You are " + str(weight_in_kgs) + " Kilograms.")
else:
    weight_in_lbs = int(weight) / 0.45
    print("You are " + str(weight_in_lbs) + " pounds.")


#  WHILE LOOPS

number = 7
while number > 5:
    print(number)
    number = number + 1


# FOR LOOP

for item in "Python for beginners":
    print(item)

for name in ["John", "Ian", "Kelvin", "Anne", "Joash", "Pedro"]:
    print(name)


# The Range function
for number in range(3, 8, 2):
    print(number)


prices = [10, 20, 30, 50, 40, 45, 3, 62]
total = 0
for price in prices:
    total = total + price
    print(total)
print(total)


# NESTED LOOPS

# Let us generate a list of co-ordinates of combination x and y values e.g (0,0), (1,0).......

prices = [10, 20, 30, 50, 40, 45, 3, 62]
total = 0
for price in prices:
    total = total + price
    print(total)
print(total)



# LISTS

names = ["Jane", "Susan", "John", "Henry", 1, 33, True, "Joshua"]
print(names[2])
names[0] = "Alphonce"
names[0] = "Peter"
print(names)


#  Write a program to find the largest number in a list
numbers = [2, 7, 9, 2, 4, 5, 2, 4, 7, 1, 44, 66, 33, 77, 22, 66, 77, 22, 9, 634, 776, 81, 543, 90, 200, 506]
maximum_number = numbers[0]
for number in numbers:
    if number > maximum_number:
        maximum_number = number
        print(maximum_number)




# 2 DIMENSION LIST (2 D List)
matrix = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[1][2] = 7
print(matrix)

# Nested for loop
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

names = ["Jane", "Susan", "John", "Henry", 1, 33, True, "Joshua"]
print(names[2])
names[0] = "Alphonce"
names[0] = "Peter"
print(names)



# LIST METHODS

# .append() -> Used to add an item at the end of a list
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)



# .insert() -> Used to add an item anywhere in the list, give the index and the item to be added
numbers = [3, 4, 7, 9, 2]
numbers.insert(1, 15)
print(numbers)



# .remove() -> Used to remove an item from a list, put the item in brackets
numbers = [3, 4, 7, 9, 2]
numbers.remove(3)
print(numbers)




# .clear() -> Used to remove all items in a list / empties our list
numbers = [3, 4, 7, 9, 2]
numbers.clear()
print(numbers)



# .pop() -> Used to remove the last item in our list
numbers = [3, 4, 7, 9, 2, 8]
numbers.pop()
print(numbers)




# .index() -> Used to check for existence of an item and return its index/ position
numbers = [3, 4, 7, 9, 2, 8]
print(numbers.index(9))




# in operator
numbers = [3, 4, 7, 9, 2, 8]
print(8 in numbers)




# .count() -> Used for counting appearences / occurrence of an item
numbers = [3, 4, 7, 9, 2, 8, 4, 4, 4]
print(numbers.count(9))




# .sort() -> Used to arrange / sort our list
numbers = [3, 4, 7, 9, 2, 8, 6, 1, 8, 5, 12, 93]
numbers.sort()
print(numbers)




# .reverse() -> Used to reverse a list
numbers = [9, 5, 2, 4, 1, 8]
numbers.reverse()
print(numbers)



# Write the list below in descending order -> numbers = [3, 5, 16, 4, 1, 8, 2, 9, 0, 4, 7, 6, 12]
numbers = [3, 5, 16, 4, 1, 8, 2, 9, 0, 4, 7, 6, 12]
numbers.sort()
numbers.reverse()
print(numbers)




# .copy() -> Used to get a copy of our list
numbers1 = [3, 5, 16, 4, 1, 8, 2, 9, 0, 4, 7, 6, 12]
numbers2 = numbers1.copy()
numbers1.append(18)
print(numbers2)
print(numbers1)



# TUPLES -> Used to store information that cannot be modified. We use paranthesis / curved brackets () TUPLES ARE IMMUTABLE

numbers = (2, 1, 2, 3, 2)
print(numbers.index(2))

# Unpacking
coordinates = (1, 2, 3, 7, 8)
x, y, z, t, p = coordinates
print(z)

simple_list = [4, 7, 9]
q, r, s = simple_list
print(s)

# DICTIONARIES
customer = {
    "name": "John Smith",
    "age": 55,
    "is_verified": True
}

print(customer["name"])
print(customer.get("age"))


customer["name"] = "Evans J."
print(customer.get("name"))

customer["birthdate"] = "January 22 1960"
print(customer)



phone = input("Enter your number: ")

my_dictionary = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output = ""
for numbers in phone:
    output += my_dictionary.get(numbers, "") + " "
print(output)




# FUNCTIONS

def message(name1, name2):
    print("Hello " + name1 + " and " + name2 + ", good morning and nice to meet all of you.")


message("John", "Kelly")


def car_cost_calculator(price, number_of_cars, percentage_discount):
    calculation = price * number_of_cars * (100 - percentage_discount)/100
    print(f"Your total cars cost is: ${calculation}")


car_cost_calculator(60000, 50, 4)


def number_to_words_converter():
    phone = input("Enter your number: ")

    my_dictionary = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine"
    }

    output = ""
    for numbers in phone:
        output += my_dictionary.get(numbers, "") + " "
    print(output)


number_to_words_converter()


# Write the list below in descending order -> numbers = [3, 5, 16, 4, 1, 8, 2, 9, 0, 4, 7, 6, 12]


def descending_order(mynumbers):
    mynumbers.sort()
    mynumbers.reverse()
    print(mynumbers)


children_age = [3, 5, 7, 2, 4, 22, 1, 12, 2, 12, 7, 13]
descending_order(children_age)


def greeting(name):
    print(f"Hello {name}!")


greeting("Ian")


def car_cost_calculator(price, number_of_cars, percentage_discount):
    calculation = price * number_of_cars * (100 - percentage_discount)/100
    print(f"Your total cars cost is: ${calculation}")


car_cost_calculator(2000, 50, 4)




def greeting(name):
    print(f"Hello {name}, welcome to my website!!")
    print("We will be happy to serve you")


greeting("Dave")
greeting("John")
greeting("Henry")
greeting("Susan")



def car_price_calculator(price, number_of_cars):
    discount = price * 0.1
    calculation = (price * number_of_cars) - discount
    output = "Total price is: $" + str(calculation)
    return output


car_price_calculator(365, 7)




def arrange_in_descending(numbers):
    numbers.sort()
    numbers.reverse()
    print(numbers)


arrange_in_descending([24, 5, 6, 1, 22, 40, 43, 333, 45, 345, 7, 8, 0])


# POSITIONAL ARGUMENTS -> Are arguments which their position matter


def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}, nice to meet you!!")


greet_user(last_name=65678987654, first_name="Johnny")


def number_to_words_converter():
    phone = input("Enter your number: ")

    my_dictionary = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine"
    }

    output = ""
    for numbers in phone:
        output += my_dictionary.get(numbers, "") + " "
    print(output)


number_to_words_converter()

# EXCEPTIONS -> Exceptions help us to handle errors (the try-except mechanism)


try:
    birth_year = input("Enter your birth year: ")
    age = 2023 - int(birth_year)
    print(f"You are {age} years old.")

except ValueError:
    print("Do not write your age in words or strings!!!")


course = "Python for beginners"
# The square bracket syntax
print(course[:-7])
print(course)

# Formatted Strings

name = "Alfred"
age = 46
print(f"Hello, {name}. You are {age} years old.")

# STRING METHODS
school = "university of the people"
print(len(school))

print(school.find("o"))

# The in Operator

fruit1 = "orange is delicious"
print("delicious" in fruit1)

# Arithmetic Operations
# -, +, %, *, /, **, //

print(10 // 3)  # Double forward slash -> Returns integer without the remainder
print(10 % 3)  # Modulus -> Returns remainder of division
print(2 ** 3)

# Augmented Assignment Operator (+= , -= , *=)
age = 10
age = age + 2
print(age)

age = 10
age += 2
print(age)


number_of_students = 0
number_of_students += 1

# Operator precedence -> BODMAS, PEMDAS

# Math Functions
# rounding off -> Look at the numbers 1, 10, 100, 1000
print(round(8.6))
x = 3
print(x * math.pi)

import math
import random

print(random.randrange(1, 10))



random_numbers = random.randrange(1, 10) # Only numbers to be considered are 1, 3, 5, 7, and 9
print(random_numbers)


dish_washer = random.choice(["Dave", "John", "Anne", "Joy", "Philip"])
print(dish_washer)


# LOGICAL OPERATORS
# The Logical and operator
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for a loan")


# The logical or operator

has_high_income = True
has_good_credit = False
is_working = True

if has_high_income and has_good_credit or is_working:
    print("Eligible for a loan")

# IN SUMMARY
# AND -> Both have to be True
# OR  -> At least one has to be True


# The logical not operator

has_high_income = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print("Eligible for a loan")


is_sick = True

if is_sick:
    print("Go to the hospital!")



# COMPARISON OPERATORS

# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
#  == Equality operator

temperature = 23

if temperature <= 7:
    print("It is a cold day")
elif temperature >= 25:
    print("It is a hot day")
else:
    print("It is neither hot nor cold")



# Name should never be less than 3 characters and name should never be more than 50 characters

name = input("Enter your name: ")

if len(name) < 3:
    print("Name cannot be less than 3 characters!!")
elif len(name) > 50:
    print("Name cannot be more than 50 characters!!")
else:
    print("Name is perfect!!")



# INFO FROM THE USER -> weight, unit
# We calculate weight in Pounds if entered was Kilograms
# We calculate weight in Kilograms if entered weight was Pounds

user_weight = input("Enter your weight: ")
unit = input("Is the weight in Pounds(L) or Kilograms(K): ")


if unit.upper() == "L":
    converted_weight = int(user_weight) * 0.45
    print(f"Your weight in kilograms is {converted_weight} kgs.")

elif unit.upper() == "K":
    converted_weight = int(user_weight) / 0.45
    print(f"Your weight in pounds is {converted_weight} pounds.")

else:
    print("Please enter either K/k or L/l")



# WHILE LOOPS

i = 1
while i <= 5:
    print(i)
    i = i + 1






i = 1
while i <= 5:
    print(i)
    i = i + 1
"""

"""

>>stop
The car has stopped

>>help
start- To start the car
stop- To stop the car
quit- To quit/exit


while True:
    command = input(">>").lower()

    if command == "start":
        print("The car has started.")

    elif command == "stop":
        print("The car has stopped.")

    elif command == "help":
        print("start- To start the car")
        print("stop- To stop the car")
        print("quit- To quit/exit")

    elif command == "quit":
        break

    else:
        print("I don't understand that!")



for letter in "Kelly":
    print(letter)


names = ["Kelly", "Ian", "Ken", "John"]
for x in names:
    print(x)



print(range(10))

for number in range(10):
    print(number)


for character in "Kelly":
    print(character)

for name in ["Ian", "Kelly", "John", "Ahmed"]:
    print(name)

for digit in [4, 6, 9, 2, 5]:
    print(digit * "*")



# Range function

for number in range(15, 51, 3):
    print(number)



prices = [4, 3.95, 12]

total = 0
for price in prices:
    total = total + price

print(f"Total: ${total}")

# (0, 0)

for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [1, 3]



# FOR LOOP

noun = "School"
for letter in noun:
    print(letter)


for name in ["Ken", "Anne", "Kelly", "Ian"]:
    print(name)

clubs = ["Arsenal", "Man Utd", "Liverpool", "Chelsea", "Man City"]
for single_club in clubs:
    print(single_club)

numbers = [1, 3, 5, 2, 7, 4, 2]
for digit in numbers:
    print(digit)



# RANGE FUNCTION
print("first")
for number in range(8):
    print(number)


print("second")
# We can give the minimum value to in the range to be considered
for item in range(5, 14):
    print(item)

print("third")
# We can add an interval to our range of values
# The interval is added as the third argument
for digit in range(3, 13, 3):
    print(digit)


# Exercise - Write a programme to calculate the total costs of all items in a shopping cart

prices = [43, 12, 20, 18, 4, 19.5, 2]

total = 0
for price in prices:
    total = total + price

print(f"The total value is: ${total}")


# NESTED LOOPS
for x in range(4):
    for y in range(4):
        print(f"({x}, {y})")

adjectives = ["red", "small", "tasty"]
fruits = ["banana", "apple", "cherry"]


for adj in adjectives:
    for fruit in fruits:
        print(f"The {fruit} is {adj}.")


# LISTS
names = ["Kelly", "Ian", "John", "Ahmed"]
print(names[1:-1])

print(names)

names[1] = "Anne"
print(names)


# 2 DIMENSIONAL LISTS (2D)

names = [
    ["Alice", "Trina", "Sophy"],
    ["Peter", "Kelly", "John"]
]

print(names[1][0])


matrix = [
    [1, 2, 10],
    [[5, 9], [22, 23], [[3],[2, 7]]],
    [3, 20, 9] ]

print(matrix[1][2][1][0])
matrix[2][1] = 7
print(matrix)


# LIST METHODS / FUNCTIONS

# .append() - Used to add a value at the end of a list
numbers = [2, 6, 9, 30]
numbers.append(99)
print(numbers)


# .insert() - used to insert a value in middle or at tye beginning of a list
numbers = [2, 6, 9, 30]
numbers.insert(2, 3)
print(numbers)

# .remove() - used to remove an item from a list
numbers = [2, 6, 9, 30]
numbers.remove(30)
print(numbers)

# .clear() - used to empty a list
numbers = [2, 6, 9, 30]
numbers.clear()
print(numbers)


# .pop() - Used to remove the last item in our list
numbers = [2, 6, 9, 30]
numbers.pop()
print(numbers)


# index - Used to check for existence of an item in a list and find its index
numbers = [2, 6, 9, 30, 5, 8, 9, 1, 3, 2, 0, 5]
print(numbers.index(9))

# The in operator - checks existence and return boolean
numbers = [2, 6, 9, 30]
print(6 in numbers)


# .count() - Used for counting the occurrences or appearances of an item
numbers = [4, 5, 3, 4, 8, 9, 1, 4, 9, 0, 5, 4, 99, 34, 6, 12, 43, 7, 4, 8, 1, 22, 32, 4, 1, 8]
print(numbers.count(1))


# .sort() - Used to arrange/sort our list in ascending/increasing order
numbers = [4, 5, 3, 4, 8, 9, 1, 4, 9, 0, 5, 4, 99, 34, 6, 12, 43, 7, 4, 8, 1, 22, 32, 4, 1, 8]
numbers.sort()
print(numbers)

# .reverse() - Used to reverse a list/ print from the last to the first
numbers.reverse()
print(numbers)

# .copy() - Used to get a copy of our list e.g lets copy list1 to create another list2
list1 = [3, 4, 5, 6, 7]
mylist = list1.copy()
print(list1)
print(mylist)


# EXERCISE - WRITE A PROGRAM THAT REMOVES ANY NUMBER APPEARING MORE THAN TWICE AND ONLY PRINTS IT ONCE
numbers = [2, 2, 4, 6, 4, 7, 2, 1, 9, 2, 6, 7, 8, 1, 0, 1, 4, 8, 7, 0]
mynewlist = []
for number in numbers:
    if number not in mynewlist:
        mynewlist.append(number)
print(mynewlist)


numbers = [2, 2, 4, 6, 4, 7, 2, 1, 9, 2, 6, 7, 8, 1, 0, 1, 4, 8, 7, 0]
unique_values = []
for number in numbers:
    if number not in unique_values:
        unique_values.append(number)
print(unique_values)


# TUPLES
# Below is an example of a tuple
numbers = (2, 3, 4)

# Methods of Tuples

# .count() - Used to count the number of occurrences of an item
my_tuple = (2, 4, 6, 2, 2, 9, 0, 2, 1, 4, 6, 7, 3)
print(my_tuple.count(2))

# .index() - Used to find the index of the first occurrence of an item
simple_tuple = (3, 5, 7, 8, 0, 1, 6, 3, 8)
print(simple_tuple.index(7))

# The in operator
simple_tuple = (3, 5, 7, 8, 0, 1, 6, 3, 8)
print(0 in simple_tuple)

# Tuples cannot be modified or changed after assignment (we cannot reassign)
numbers = (2, 3, 4)
numbers[1] = 48
print(numbers)


# UNPACKING
marks = (79, 83, 81)
John, Mark, Kelly = marks
print(Kelly,  Mark, John)


name1 = "Anne"
name2 = "Smith"
print(name1, name2)


ages = [13, 14, 76]
Joy, Antony, Daniel = ages
print(Daniel, Joy)


# DICTIONARIES
customer1 = {
    "Name": "John Smith",
    "age": 57,
    "is_working": True
}

customer2 = {
    "Name": "Ian Geoff",
    "age": 27,
    "is_working": False
}

company = {
    "name": "Tesla",
    "number_of_workers": 505,
    "number_of_branches": 21,
    "is_registered": True,
    "paid_taxes": True,
    "yearly_revenue": 2000000
}

print(customer2["Name"])

# In a dictionary we have key value pairs. e.g "name" ia a key and "John Smith" ia a value
# This is how we can access the value of any key in a dictionary
print(company["name"])

company["name"] = "TESLA WORLD"
company["yearly_revenue"] = 1010110
print(company)


dictionary = {
    "walk": "lifting and settling down each foot in turn to move",
    "run": "to walk very fast",
    "chair": "a seat",
    "car": "a four wheeled vehicle that can carry small number of people"
}

print(dictionary["car"])


company = {
    "name": "Tesla",
    "number_of_workers": 505,
    "number_of_branches": 21,
    "is_registered": False,
    "paid_taxes": True,
    "yearly_revenue": 2000000
}

print(company["name"])

# In a dictionary we have key value pairs. e.g "name" is a key and "Tesla" ia a value
# This is how we can access the value of any key in a dictionary
print(company["is_registered"])

# We can change the values of our dictionary
company["name"] = "TESLA WORLD"  # Reassignment
print(company["name"])
company["yearly_revenue"] = 1000000
print(company)



# Let us write a programme that asks our phone number and then prints it in words

phone_number = input("Enter your phone number: ")

digit_word_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}

output = ""

for number in phone_number:
    output += digit_word_mapping.get(number, "*") + " "

print(f"This is your number in words: {output}")






# Let us write a programme that asks our phone number and then prints it in words

phone_number = input("Enter your phone number: ")

digit_word_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output = ""

for number in phone_number:
    output += digit_word_mapping.get(number, "?") + " "

print(f"This is your number in words: {output}")


# parameter and argument
def greeting(name1, name2, message):
    print(f"Hello {name1} {name2}!")
    print("How are you doing?")
    print(message)


greeting("Alfred", "Hussein", "Have a great day!!")



def price_calculator(basic_price, discount, commission, tax, shipping_cost):
    final_price = basic_price - discount - commission + tax + shipping_cost
    return print(f"The total payable cost is: ${final_price}")


# keyword argument

price_calculator(discount=200, tax=15, basic_price=20000, shipping_cost=50, commission=35)


# Let us write a programme that asks our phone number and then prints it in words


def number_to_word_converter():

    phone_number = input("Enter your phone number: ")

    digit_word_mapping = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine"
    }

    output = ""

    for number in phone_number:
        output += digit_word_mapping.get(number, "!") + " "

    return f"This is your number in words: {output}"


print(number_to_word_converter())


# EXCEPTIONS

try:
    age = int(input("Age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Age must be a numerical value!!")



try:
    def division_calculator(first_number, second_number):
        answer = first_number / second_number
        return print(f"The answer for your division is {answer}")
    division_calculator(77, 4)

except ZeroDivisionError:
    print("The second cannot be Zero.")



# Object-oriented programming (OOP)
class MyClass:
    x = 5


# class
class Point:
    def move(self):
        print("Move.................")

    def draw(self):
        print("Drawing,,,")

    def stop(self):
        print("iuytrertyuil")


# object
duck = Point()
duck.stop()
# attributes
duck.number = 3
duck.y = True
duck.name = "this is an attribute ..."
print(duck.number)

me = Point()
me.move()
me.x = 18
me.y = "5"


class Car:
    def drive(self):
        print("Driving the car")

    def hire(self):
        print("Hiring the car")


daniel = Car()  # Object
daniel.hire()
daniel.injured = True  # Attribute

alphonce = Car()
alphonce.drive()
alphonce.message = "I won't be available"


# The __init__() Function



class Person:
    def __init__(self, age, name, height, is_sick):
        self.name = name
        self.age = age
        self.height = height
        self.is_sick = is_sick
    def run(self):
        print("This person is running")


person1 = Person(21, "David", 1.6, True)
person2 = Person(55, "Alphonce", 1.8, False)
person3 = Person(29, "Ian", 1.5, False)

print(person2.name)

person1.run()
person1.is_black = True

print(person1.is_black)



# PYTHON INHERITANCE


class Animals: # The parent class
    def walk(self):
        print("It is walking..")
    def run(self):
        print("It is running..")

my_animal = Animals()
my_animal.walk()
my_animal.run()

class Dog(Animals): # The child class
    def bark(self):
        print("Its is barking..")


my_puppy = Dog()
my_puppy.run()
my_puppy.bark()
my_puppy.walk()


# DRY Don't Repeat Yourself

import converters
from converters import kg_to_lbs, lbs_to_kgs

print(kg_to_lbs(100))
print(lbs_to_kgs(75))


from shipping.calculator import shipping_calculator

shipping_calculator()
"""

# Generating Random Values

# 1) The random method
import random

for i in range(3):
    print(random.random())

# 2) The randint method

for i in range(3):
    print(random.randint(93, 100))

# 3) The random.choice

members = ["David", "Joy", "Philip", "Andrew"]
chosen_person = random.choice(members)
print(chosen_person)
