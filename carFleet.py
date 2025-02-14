# Car Fleet
# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.

# Example 1:

# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

# Constraints:

# n == position.length == speed.length.
# 1 <= n <= 1000
# 0 < target <= 1000
# 0 < speed[i] <= 100
# 0 <= position[i] < target
# All the values of position are unique.

# solution
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create pairs, zip would pair the each index from each list 1,1 2,2 3,3 etc
        pair = [(p, s) for p, s in zip(position, speed)]
        # sort the list in reverse order making it so we look at it from the car that is closest to the target
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            # append to the stack the ammount of time it takes to get to the target
            stack.append((target - p) / s)
            # after appending to the stack check if the stack is greater than or equal to a length of 2
            # if the stack has 2 or more elements check if the most recent element arrives faster or equals the element before it
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # if both cases are true then remove the most recent element
                stack.pop()
        # return stack length
        return len(stack)