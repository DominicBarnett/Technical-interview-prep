# Binary Search
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in 
# O
# (
# l
# o
# g
# n
# )
# O(logn) time.

# Example 1:

# Input: nums = [-1,0,2,4,6,8], target = 4

# Output: 3
# Example 2:

# Input: nums = [-1,0,2,4,6,8], target = 3

# Output: -1
# Constraints:

# 1 <= nums.length <= 10000.
# -10000 < nums[i], target < 10000

# solution
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set pointers
        l,r = 0, len(nums) - 1
        # while left pointer is less than right pointer
        while l <= r:
            # midpoint = (left index + right index) ÷ 2
            # finding the midpoint of the array
            m = (l + r) // 2
            # if the value of the midpoint is greater than the target
            if nums[m] > target:
                # move the right pointer one index to the left of the midpoint
                r = m - 1
            # if the value of the midpoint is less than the target
            elif nums[m] < target:
                # move the left pointer one index to the right of the midpoint
                l = m + 1
            else:
                # if the midpoint value == target return m
                return m
        # if the target wasn't found return -1
        return -1