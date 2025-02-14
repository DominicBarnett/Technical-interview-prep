# Search a 2D Matrix
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Example 1:



# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true
# Example 2:



# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

# Output: false
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10000 <= matrix[i][j], target <= 10000

# solution

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        t, b = 0, ROWS - 1  # Top and bottom row pointers

        # Step 1: Binary search to find the correct row
        while t <= b: 
            vM = (t + b) // 2  # Find the middle row
            if matrix[vM][0] <= target <= matrix[vM][-1]:  
                # If the target is within this row's range, stop searching
                break  
            elif matrix[vM][-1] < target:
                # If the target is greater than the last element of this row, search below
                t = vM + 1
            else:
                # If the target is smaller than the first element of this row, search above
                b = vM - 1

        if not (t <= b):  
            # If the binary search went out of bounds, the target is not in any row
            return False

        row = (t + b) // 2  # The row where the target may be found
        l, r = 0, COLS - 1  # Left and right pointers for column search

        # Step 2: Binary search within the selected row
        while l <= r:
            m = (l + r) // 2  # Find the middle column index
            if matrix[row][m] > target:
                # If the middle element is greater than the target, search the left half
                r = m - 1
            elif matrix[row][m] < target:
                # If the middle element is smaller, search the right half
                l = m + 1
            else:
                # If found, return True
                return True

        return False  # If not found after searching the row, return False
