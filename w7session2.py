"""

Problem 1: Finding the Perfect Cruise
It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, 
use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.

def find_cruise_length(cruise_lengths, vacation_length):
    pass
Example Usage:

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
Example Output:

True
False

U: given an int vacation_length (13), and list cruise lengths in ascending
binary search iff return true if searching for the cruise length

M: binary search (aka 3 pointers, left mid right)

P:

left, right , middle pointers
middle = (left + right) // 2
loop if left > right

 if cruise_length[mid] > vacation_length:
    right = mid - 1
 elif cruise_length[mid] < vacation_length:
    left = mid + 1
 else:
      return True

 return false

"""

def find_cruise_length(cruise_lengths, vacation_length):
    #left, right , middle pointers
    left = 0
    right = len(cruise_lengths) - 1
    # loop if left > right
    while left <= right:
     
        middle = (left + right) // 2
        if cruise_lengths[middle] > vacation_length:
            right = middle - 1
        elif cruise_lengths[middle] < vacation_length:
            left = middle + 1
        else:
            return True

    return False 
    
# left = 1 right = 6 middle = 3 

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
