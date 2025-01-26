// Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

// An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

// Example 1:

// Input: s = "racecar", t = "carrace"

// Output: true
// Example 2:

// Input: s = "jar", t = "jam"

// Output: false
// Constraints:

// s and t consist of lowercase English letters.


// class Solution {
//     /**
//      * @param {string} s
//      * @param {string} t
//      * @return {boolean}
//      */
//     isAnagram(s, t) {
//         if (s.length !== t.length) {
//             return false;
//         }

//         let sSort = s.split("").sort().join();
//         let tSort = t.split("").sort().join();
//         return sSort == tSort
//     }
// }

// Hashtable solution
class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // if the lengths aren't the same then they aren't anagrams
        if (s.length !== t.length) {
            return false;
        }

        // initialize dictionaries
        const countS = {};
        const countT = {};
        // since the length of the strings are the same we can count from either one
        for (let i = 0; i < s.length; i++) {
            // for the string s take the character at index i and make that a key in the dictionary set the value of that key to the amount of times it appears in the string
            // at the same time do the same process for the second string
            countS[s[i]] = (countS[s[i]] || 0) + 1;
            countT[t[i]] = (countT[t[i]] || 0) + 1;
        }

        // check if the keys and counts match in both dictionaries
        for (const key in countS) {
            if (countS[key] !== countT[key]) {
                return false;
            }
        }
        return true;
    }
}