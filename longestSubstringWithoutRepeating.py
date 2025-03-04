# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.

# solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}  # HashMap to store the last index of characters
        l = 0  # Left pointer for the sliding window
        res = 0  # Stores the max length of unique substring
        
        for r in range(len(s)):  # Right pointer iterates through the string
            if s[r] in mp:
                # If the character is already in the window, move 'l' past its last occurrence
                l = max(mp[s[r]] + 1, l)
            
            # Store the current character's index
            mp[s[r]] = r  
            
            # Update the max length of unique substring found
            res = max(res, r - l + 1)
        
        return res  # Return the longest substring length
