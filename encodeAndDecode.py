# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # if string is empty return empty string
        if not strs:
            return ""
        # initialize variables
        sizes, res = [], ""
        # for index in list of strings
        for s in strs:
            # append the lenth of each index to sizes list
            sizes.append(len(s))
        for sz in sizes:
            # for index in sizes convert index to a string
            res += str(sz)
            # Add a comma after index
            res += ','
        # once all sizes have been accounted for add a "#"
        res += '#'
        # add each string from initial list to the end of the res string
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        # while index of the string is not "#"
        while s[i] != '#':
            cur = ""
            # While index of the string is not ","
            while s[i] != ',':
                # add the number before the , to the temp string cur
                cur += s[i]
                # iterate then run into a comma and stop the while loop
                i += 1
            # append the number before the , to the sizes array as an integer
            sizes.append(int(cur))
            # iterate and continue until you hit a #
            i += 1
        # iterate by one to pass the #
        i += 1

        # for i in sizes 
        for sz in sizes:
            #  result.append starting at one index past the # move index plus the size stored in the sizes array
            res.append(s[i:i + sz])
            # increase count by the size of the string previously output
            i += sz
        return res