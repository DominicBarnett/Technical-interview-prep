# Koko Eating Bananas
# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

# Return the minimum integer k such that you can eat all the bananas within h hours.

# Example 1:

# Input: piles = [1,4,3,2], h = 9

# Output: 2
# Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

# Example 2:

# Input: piles = [25,10,23,4], h = 4

# Output: 25
# Constraints:

# 1 <= piles.length <= 1,000
# piles.length <= h <= 1,000,000
# 1 <= piles[i] <= 1,000,000,000

# solution
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Step 1: Initialize binary search boundaries
        l, r = 1, max(piles)  # k must be between 1 and the largest pile
        res = r  # Store the minimum speed

        # Step 2: Perform binary search
        while l <= r:
            k = (l + r) // 2  # Middle point (potential eating speed)

            # Step 3: Calculate total time needed with speed k
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)  # Time for each pile
            
            # Step 4: Check if time fits within the allowed hours
            if totalTime <= h:
                res = k  # Update the result with a valid minimum speed
                r = k - 1  # Try a smaller speed
            else:
                l = k + 1  # Increase speed if time exceeds allowed hours

        # Step 5: Return the smallest valid speed
        return res