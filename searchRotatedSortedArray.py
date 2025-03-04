# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

# You may assume all elements in the sorted rotated array nums are unique,

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:

# Input: nums = [3,4,5,6,1,2], target = 1

# Output: 4
# Example 2:

# Input: nums = [3,5,6,0,1,2], target = 4

# Output: -1
# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -1000 <= target <= 1000

# solution
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Step 1: Find the pivot index (smallest element)
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:  
                # Pivot is in the right half
                l = m + 1
            else:
                # Pivot is at m or in the left half
                r = m  
        
        pivot = l  # This is the index of the smallest element

        # Step 2: Perform binary search in the correct sorted half
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1  # Target not found

        # Search in the left half before pivot
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result  # If found in first half, return index

        # Search in the right half from pivot to end
        return binary_search(pivot, len(nums) - 1)
