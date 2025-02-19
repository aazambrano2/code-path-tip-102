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
