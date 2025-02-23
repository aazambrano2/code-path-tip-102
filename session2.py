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


"""
Problem 4: Two-Pointer Two Sum
Use the two pointer approach to implement a function two_sum() 
that takes in a sorted list of integers nums and an integer target as parameters 
and returns the indices of the two numbers that add up to target. 
You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the indices in any order.

def two_sum(nums, target):
    pass
Example Usage

nums = [2, 7, 11, 15]
target = 9
two_sum(nums, target)

nums = [2, 7, 11, 15]
target = 18
two_sum(nums, target)
Example Output:

[0, 1]
[1, 2]
"""

def two_sum(nums, target):

    left = 0
    right = len(nums) - 1
    index = []
    while left < len(nums):
        if nums[left] + nums[right] == target:
            index =  [left,right]
            break
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return index

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))

"""
Problem 5: Three Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

def three_sum(nums):
    pass
Example Usage

nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)

nums = [0, 1, 1]
three_sum(nums)

nums = [0, 0, 0]
three_sum(nums)
Example Output:

[[-1, -1, 2], [-1, 0, 1]]
[]
[[0, 0, 0]]
💡Hint: Sorting Lists
"""

def three_sum(nums):
    nums.sort()
    answer = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue
        
        j, k = i + 1, len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                answer.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                
                while j < k and nums[j] == nums[j - 1]:  # Skip duplicates
                    j += 1
                while j < k and nums[k] == nums[k + 1]:  # Skip duplicates
                    k -= 1
            
            elif total < 0:
                j += 1
            else:
                k -= 1

    return answer


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))



"""
Problem 6: Insert Interval
Implement a function insert_interval() that accepts an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. The function also accepts an interval new_interval = [start, end] that represents the start and end of another interval.

Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

You don't need to modify intervals in-place. You can make a new array and return it.

def insert_interval(intervals, new_interval):
    pass
Example Usage

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
insert_interval(intervals, new_interval)

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
insert_interval(intervals, new_interval)
Example Output:

[[1, 5], [6, 9]]
[[1, 2], [3, 10], [12, 16]]

"""