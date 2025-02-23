'''
Problem 1: Transpose Matrix
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

3x3 matrix before and after being transposed

def transpose(matrix):
    pass
Example Usage

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)
Example Output:

[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
[
    [1, 4],
    [2, 5],
    [3, 6]
]
'''

def transpose(matrix):
    #create transpose array
    
    transpose = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    #fill in array
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]

    print(transpose)


    return transpose

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)

'''
Problem 5: Container with Most Honey
Christopher Robin is helping Pooh construct the biggest hunny jar possible. Help his write a function that accepts an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.

def most_honey(height):
	pass
Bar graph showing heights of lines in Example 1, with blue section between lines with height 8 and 7

Example Usage

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)
Example Output:

49
1
'''

def most_honey(height):

    left = 0 
    right = len(height) - 1 
    max_area = 0

    while left < right:
        width = right - left
        h = min(height[right],height[left])
        area = width * h
        max_area = max(max_area,area)
        
        if height[left] < height[right]:
            left += 1
        else: right -= 1
    print(max_area)
    return max_area

height = [1, 1, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)


#advance problem set v2

"""
Problem 1: Matrix Addition
Write a function add_matrices() that accepts to n x m matrices matrix1 and matrix2. 
The function should return an n x m matrix sum_matrix that is the sum of the given matrices such that each value in sum_matrix 
is the sum of values of corresponding elements in matrix1 and matrix2.

def add_matrices(matrix1, matrix2):
    pass
Example Usage

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

add_matrices(matrix1, matrix2)
Example Output:

[
    [10, 10, 10],
    [10, 10, 10],
    [10, 10, 10]
]

"""

def add_matrices(matrix1,matrix2):

    sum_matrix =[[0 for _ in range(len(matrix1))] for _ in range(len(matrix[0]))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return sum_matrix

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2))

"""
Problem 2: Two-Pointer Palindrome
Write a function is_palindrome() that takes in a string s as a parameter 
and returns True if the string is a palindrome and False otherwise. 
You may assume the string contains only lowercase alphabetic characters.

The function must use the two-pointer approach,
 which is a common technique in which we initialize two variables 
 (also called a pointer in this context) to track different indices or places in a list or string, 
 then moves the pointers to point at new indices based on certain conditions. 
 In the most common variation of the two-pointer approach, 
 we initialize one variable to point at the beginning of a list 
 and a second variable/pointer to point at the end of list.
 We then shift the pointers to move inwards through the list towards each other, 
 until our problem is solved or the pointers reach the opposite ends of the list.

def is_palindrome(s):
    pass
Example Usage

s = "madam"
is_palindrome(s)

s = "madamweb"
is_palindrome(s)
Example Output:

True
False
"""

def is_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "madam"
print(is_palindrome(s))

s = "madamweb"
print(is_palindrome(s))

"""
Problem 3: Squash Spaces
Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result should be trimmed. Do not use any of the built-in trim methods.

def squash_spaces(s):
    pass
Example Usage

s = "   Up,     up,   and  away! "
squash_spaces(s)

s = "With great power comes great responsibility."
squash_spaces(s)
Example Output:

"Up, up, and away!"
"With great power comes great responsibility."

"""

def squash_spaces(s):
    return " ".join(s.split())



s = "   Up,     up,   and  away! "
print(squash_spaces(s))

s = "With great power comes great responsibility."
print(squash_spaces(s))