# PYTHON REVISION


"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





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

# Allow user enter their weight in either kilograms or pounds and convert it

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
"""

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

# Operator precedence
# BODMAS, PEMDAS
