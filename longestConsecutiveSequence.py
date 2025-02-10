# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9


# solution
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get rid of duplicates using set
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # if the previous number to the one we are looking at exists then it's not the start of a sequence. Skip it
            if (num - 1) not in numSet:
                length = 1
                # loop from the start of the sequence and see if the next number is within the set
                while (num + length) in numSet:
                    # if found add 1 to the length
                    length += 1
                # compares the length at the end of the loop to previous created loops and takes the longer sequence
                longest = max(length, longest)
        return longest