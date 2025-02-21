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