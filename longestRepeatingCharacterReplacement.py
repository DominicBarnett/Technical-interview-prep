# Longest Repeating Character Replacement
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5
# Constraints:

# 1 <= s.length <= 1000
# 0 <= k <= s.length

# solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # HashMap to store character frequencies
        res = 0  # Stores the max length of valid substring
        
        l = 0  # Left pointer for the sliding window
        maxf = 0  # Tracks the highest frequency of any single character
        
        for r in range(len(s)):  # Right pointer iterates through the string
            count[s[r]] = 1 + count.get(s[r], 0)  # Increase count of current character
            maxf = max(maxf, count[s[r]])  # Update max frequency in the window

            # Check if the number of characters that need replacement exceeds k
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # Remove leftmost character from the window
                l += 1  # Move the left pointer forward
            
            # Update max length of a valid substring
            res = max(res, r - l + 1)

        return res  # Return the longest valid substring length
