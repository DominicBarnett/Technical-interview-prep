#   Group Anagrams
#   Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

#   An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

#   Example 1:

#   Input: strs = ["act","pots","tops","cat","stop","hat"]

#   Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#   Example 2:

#   Input: strs = ["x"]

#   Output: [["x"]]
#   Example 3:

#   Input: strs = [""]

#   Output: [[""]]
#   Constraints:

#   1 <= strs.length <= 1000.
#   0 <= strs[i].length <= 100
#   strs[i] is made up of lowercase English letters.

#   Solution
#   loop through each index storing the length of the index
#   seperate indexes by length storing each in it's own hash map
#   then use logic for validating single anagrams and return the lists that have anagrams
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize a hash map to track the values to be returned
        res = defaultdict(list)
        # for each index in the given list
            # sort each index alphabetically then join it
            # push the sorted string as a key in the dictionary which initializes it with an empty list and at the same time 
            # append the unsorted string to the nested list
            # return the values of each list
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())