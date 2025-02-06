# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # set variable = to length of nums array
        n = len(nums)
        # initialize res array of 0's with a length equal to the nums array
        res = [0] * n

        # for i in length of nums array
        for i in range(n):
            # set product = 1
            prod = 1
            # for index in length of nums array
            for j in range(n):
                # if outer index equals inner index continue by one index
                if i == j:
                    continue 
                # set prod equal to prod times nums[j]   
                prod *= nums[j]
            
            # set the res[outter index] equal to the products from inner index
            res[i] = prod
            
        return res