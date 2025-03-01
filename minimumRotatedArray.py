# Find Minimum in Rotated Sorted Array
# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:

# Input: nums = [3,4,5,6,1,2]

# Output: 1
# Example 2:

# Input: nums = [4,5,0,1,2,3]

# Output: 0
# Example 3:

# Input: nums = [4,5,6,7]

# Output: 4
# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000

# solution
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the result with the first element
        res = nums[0]
        
        # Set up binary search boundaries
        l, r = 0, len(nums) - 1

        while l <= r:
            # If the current segment is already sorted, the leftmost element is the minimum
            if nums[l] < nums[r]:  
                res = min(res, nums[l])
                break  # No need to search further
            
            # Find the middle index
            m = (l + r) // 2  
            
            # Update the minimum found so far
            res = min(res, nums[m])

            # Determine which half to search next
            if nums[m] >= nums[l]:  
                # Left half is sorted, so the pivot (minimum) must be in the right half
                l = m + 1
            else:
                # Right half is sorted, meaning the pivot is in the left half
                r = m - 1
        
        return res  # Return the minimum element found
