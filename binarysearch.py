"""
Imagine you are helping a student during Study Hall. 
Teach them how to use the binary search algorithm to find an item in a sorted array. 
Your answer should provide the target number and its index. If the item is not in the array, return -1. 
Please use Python in your explanation. 
Screen sharing as you review the problem is encouraged.
"""

def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
      mid = (left + right) // 2
      if arr[mid] == target:
         return mid
      
      if arr[mid] < target:
       left = mid + 1
      if arr[mid] > target:
       right = mid - 1 
      
    return -1

print(binary_search([1,2,3,4,5,6,7,8],6))
print(binary_search([1],0))