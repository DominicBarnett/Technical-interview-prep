# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100

# solution
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # Initialize buy (l) and sell (r) pointers
        maxP = 0  # Store maximum profit found

        while r < len(prices):  # Loop until we reach the end
            if prices[l] < prices[r]:  
                # If the selling price is higher than the buying price, calculate profit
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)  # Update max profit if this profit is larger
            else:
                # If the price at r is lower, move the buying day to r
                l = r  
            r += 1  # Move to the next day
        
        return maxP  # Return the maximum profit
