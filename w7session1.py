
'''

Thanos is collecting Infinity Stones. Given an array of integers stones representing the power of each stone, return the total power 
using a recursive approach.

Evaluate the time complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def sum_stones(stones):
    pass
Example Usage:

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
Example Output:

105
68

u: given an array on ints, return the toal power using a recursive approach
m: recusion
p:

  base case: if len(stones) == 0: return 0

  return stone[0] + sum_stone(stones[1:])
'''
#i
def sum_stones(stones):
    if len(stones) == 0: 
        return 0
    return stones[0] + sum_stones(stones[1:])

#R
print(sum_stones([5, 10, 15, 20, 25, 30])) # 105
# 5 + 100
# 10 + 90
# 15 + 75
# 20 + 55
# 25 + 30
# 30 + 0
# 0

print(sum_stones([12, 8, 22, 16, 10])) # 68
# E
#Time Complexity: O(n)
# Space Complexity: O(n)
