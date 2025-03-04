# Permutation in String
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false
# Constraints:

# 1 <= s1.length, s2.length <= 1000

# solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # If s1 is longer than s2, s2 cannot contain a permutation
            return False
        
        # Frequency arrays for s1 and s2 window
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # Initialize frequency counts for s1 and the first len(s1) characters in s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1  # Count characters in s1
            s2Count[ord(s2[i]) - ord('a')] += 1  # Count characters in the first window of s2
        
        # Count how many characters have matching frequencies
        matches = sum(1 for i in range(26) if s1Count[i] == s2Count[i])

        # Sliding window technique
        l = 0  # Left pointer for the sliding window
        for r in range(len(s1), len(s2)):  # Right pointer expands the window
            if matches == 26:  # If all characters match, a permutation is found
                return True
            
            # Add the new character at s2[r] to the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:  # If frequency matches, increase matches
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:  # If frequency exceeded, decrease matches
                matches -= 1

            # Remove the old character at s2[l] from the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:  # If frequency matches, increase matches
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:  # If frequency dropped, decrease matches
                matches -= 1
            l += 1  # Move left pointer to maintain window size

        return matches == 26  # Check one last time after the loop
