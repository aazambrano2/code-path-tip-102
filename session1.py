#Standard Problem Set V1

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


"""
Problem 12: Thistle Hunt
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". 
The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
	pass
Example Usage

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
Example Output:

[0, 3]
[]
"""

def locate_thistles(itmes):

    indexes = [i for i, item in enumerate(itmes) if item == "thistle"]
    print(indexes)
    return indexes

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)

#Standard Problem Set V2

"""
Problem 1: Batman
Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".

def batman():
	pass
Example Usage:

batman()
Example Output:

I am vengeance. I am the night. I am Batman!

"""

def batman():
    print("I am vengeance. I am the night. I am Batman!")

batman()

"""
Problem 2: Mad Libs
Write a function madlib() that accepts one parameter, a string verb. 
The function should print the sentence: "I have one power. I never <verb>. - Batman".

def madlib(verb):
	pass
Example Usage

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)
Example Output:

"I have one power. I never give up. - Batman"
"I have one power. I never nap. - Batman"
"""

def madlib(verb):

    print(f"I have one power. I never {verb} - Batman")

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)

"""
Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."

def trilogy(year):
	pass
Example Usage:

year = 2008
trilogy(year)

year = 1998
trilogy(year)
Example Output:

"The Dark Knight"
"Christopher Nolan did not release a Batman movie in 1998."

"""

def trilogy(year):

    if year == 2005: print(" Batman Begins")
    elif year == 2008: print("The Dark Knight")
    elif year == 2012: print("The Dark Knight Rises")
    else: print(f"Christopher Nolan did not release a Batman movine in {year}")

year = 2008
trilogy(year)

year = 1998
trilogy(year)

"""
Problem 4: Last
Implement a function get_last() that accepts a list of items items and returns the last item in the list. 
If the list is empty, return None.

def get_last(items):
	pass
Example Usage

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)
Example Output:

"black adam"
None

"""
def get_last(items):

    if len(items) == 0: return None
    else: return items[-1]

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
print(get_last(items))

items = []
print(get_last(items))


"""
Problem 5: Concatenate
Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.

def concatenate(words):
	pass
Example Usage

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)
Example Output:

"vengeancedarknessbatman"
""

"""

def concatenate(words):
    if len(words) == 0: return ""
    s = ""
    for w in words:
        s += w
    #return "".join(words)
    print(s)    
    return s
words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)

"""
Problem 6: Squared
Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.

def squared(numbers):
	pass
Example Usage

numbers = [1, 2, 3]
squared(numbers)
Example Output:

[1, 4, 9]
"""

def squared(numbers):

    numbers = [n** 2 for n in numbers]
    return numbers

numbers = [1, 2, 3]
print(squared(numbers))

"""
Problem 7: NaNaNa Batman!
Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.

def nanana_batman(x):
	pass
Example Usage

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
Example Output:

"nananananana batman!"
"batman!"
"""

def nanana_batman(x):

    for i in range(1, x + 1):
        print("na",end= "")
    print(" batman!")
    #print("na" * x + " batman!")
x = 6
nanana_batman(x)

x = 0
nanana_batman(x)

"""
Problem 8: Find the Villain
Write a function find_villain() that accepts a list crowd 
and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.

def find_villain(crowd, villain):
	pass
Example Usage

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)
Example Output:

[1, 4, 6]
"""

def find_villain(crowd, villain):

    #indexes = [i for i, person in enumerate(crowd) if person == villain]

    indexes = []

    for i in range(len(crowd)):
        if crowd[i] == villain:
            indexes.append(i)

    return indexes

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain))

"""
Problem 9: Odd
Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.

def get_odds(nums):
	pass
Example Usage

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)
Example Output:

[1, 3]
[]
"""

def get_odds(nums):

    odds = [ n for n in nums if n % 2 != 0]
    print(odds)
    return odds

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)


"""
Problem 10: Up and Down
Write a function up_and_down() that accepts a list of integers lst as a parameter.
The function should return the number of odd numbers minus the number of even numbers in the list.

def up_and_down(lst):
	pass
Example Usage

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)
Example Output:

1
3
-4
"""

def up_and_down(lst):

    # odd = len([n for n in lst if n % 2 != 0])
    # even = len([n for n in lst if n % 2 == 0])

    odd = 0
    even = 0

    for n in lst:
        if n % 2 != 0: odd += 1
        else: even += 1
    print(odd-even)
    return odd - even

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)


"""
Problem 11: Running Sum
Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman has stopped each month in Gotham City. 
The function should modify the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). 
You must modify the list in place; you may not create any new lists as part of your solution.

def running_sum(superhero_stats):
	pass
Example Usage

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)
Example Output:

[1, 3, 6, 10]
[1, 2, 3, 4, 5]
[3, 4, 6, 16, 17]

"""
def running_sum(superhero_stats):

    for i in range(1, len(superhero_stats)):
        superhero_stats[i] += superhero_stats[i - 1]
    print(superhero_stats)
    return superhero_stats

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)

"""

Problem 12: Shuffle
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. 
Return the list in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(cards):
	pass
Example Usage

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
Example Output:

['Joker', 3, 'Queen', 'Ace', 2, 7]
[9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
[10, 2, 10, 2]

"""

def shuffle(cards):

    n = len(cards) // 2
    ans = []

    for i in range(n):
        ans.append(cards[i])
        ans.append(cards[i + n])
    print(ans)
    return ans
cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
