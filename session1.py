'''
Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".

def welcome():
	pass
Example Usage:

welcome()
Example Output:

Welcome to The Hundred Acre Wood!

'''

def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

'''
Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greeting(name):
	pass
Example Usage:

greetings("Michael")
greetings("Winnie the Pooh")
Example Output:

Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.

'''

def greeting(name):

    print("Welcome to the Hundred Acre Wood " + name + " My name is Christopher Robin")

greeting("Michael")


'''
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...

def print_todo_list(task):
	pass
Example Usage

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
Example Output:

Pooh's To Dos:
1. Count all the bees in the hive
2. Chase all the clouds from the sky
3. Think
4. Stoutness Exercises

Pooh's To Dos:
'''

def print_todo_list(task):

    print("Pooh's to Dos:")

    for index, statement in enumerate(task):
        print(f"{index + 1}." + statement)

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

'''
Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.

def count_less_than(race_times, threshold):
	pass
Example Usage

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)
Example Output:

3
0
'''

def count_less_than(race_times, threshold):
    count = 0

    for time in race_times:
        if time < threshold:
            count += 1  
    print(count)      
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)


"""
Problem 3: Catchphrase
Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

Character	Catchphrase
"Pooh"	"Oh bother!"
"Tigger"	"TTFN: Ta-ta for now!"
"Eeyore"	"Thanks for noticing me."
"Christopher Robin"	"Silly old bear."
If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"

def print_catchphrase(character):
	pass
Example Usage

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)
Example Output:

"Oh bother!"
"Sorry! I don't know Piglet's catchphrase!"

"""

def print_catchphrase(character):
   if character.lower() == "pooh": print("oh brother!")
   elif character.lower() == "tigger": print(" TTFN: Ta-ta for now!")
   elif character.lower() == "eeyore": print(" Thanks for noticing me")
   elif character.lower() == "christopher robin": print("Silly old bear")
   else: print(f"Sorry! I don't know {character}'s catchphrase!")
    
character = "Pooh"
print_catchphrase(character)

"""
Problem 5: Total Honey
Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().

def sum_honey(hunny_jars):
	pass
Example Usage

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)
Example Output:

14
0

"""

def sum_honey(hunny_jars):

    sum = 0

    for jar in hunny_jars:
        sum += jar
    return sum

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))

"""
Problem 6: Double Trouble
Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.

def doubled(hunny_jars):
	pass
Example Usage

hunny_jars = [1, 2, 3]
doubled(hunny_jars)
Example Output:

[2, 4, 6]
"""

def doubled(hunny_jars):

    hunny_jars = [jar*2 for jar in hunny_jars]

    return hunny_jars

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

"""
Problem 9: Pairs
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise.

def can_pair(item_quantities):
	pass
Example Usage

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)
Example Output:

True
False
True

"""

def can_pair(item_quantities):

    for item in item_quantities:
        if item % 2 != 0: return False
    return True


item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

"""
Problem 10: Split Haycorns
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. 
split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.

def split_haycorns(quantity):
	pass
Example Usage

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)
Example Output:

[1, 2, 3, 6]
[1]
"""

def split_haycorns(quantity):

    divisors = [i for i in range(1, quantity + 1) if quantity % i == 0]

    return divisors

quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))

"""
Problem 11: T-I-Double Guh-ER
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. 
Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.

def tiggerfy(s):
	pass
Example Usage

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
Example Output:

"suspcous"
""
"Hunny"

"""

def tiggerfy(s):

    s = [c for c in s if c.lower() not in "tiger"]

    return "".join(s)

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))