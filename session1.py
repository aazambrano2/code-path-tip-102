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