# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.

# solution
# create a hash map
# loop through the list and create a key for any unknown number and initialize the values to 1 then anytime it is seen again increase count by 1
# loop through the keys and find the biggest then store it and remove it from the dictionary then repeat for k
# return the top k
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary for frequency
        count = {}
        # for i in nums initialize the i as a key then set the value to 1 + if i already exists whatever its value is currently
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # set a list with key values
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        # sort the list lowest to highest frequency
        arr.sort()

        res = []
        while len(res) < k:
            # while the length of a return list is less than k remove the last element from the frequency list and story it's value in the return list
            res.append(arr.pop()[1])
        return res