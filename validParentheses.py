# Valid Parentheses
# Solved 
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000



# solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # hash map to track closing character to their open character
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # for character in string
        for c in s:
            # if character is a closing bracket
            if c in closeToOpen:
                # if the stack isn't empty and the item at the top of the stack is an opening bracket (matches the value of c)
                if stack and stack[-1] == closeToOpen[c]:
                    # remove the matching opening pair
                    stack.pop()
                else:
                    return False
            else:
                # else add the opening bracket to the top of the stack
                stack.append(c)
        
        return True if not stack else False