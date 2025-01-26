// Problem 1

// Contains Duplicate
// Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

// Example 1:

// Input: nums = [1, 2, 3, 3]

// Output: true

// Example 2:

// Input: nums = [1, 2, 3, 4]

// Output: false

// class Solution {
//     /**
//      * @param {number[]} nums
//      * @return {boolean}
//      */
//     hasDuplicate(nums) {
//         for (let i = 0; i < nums.length; i++) {
//             for (let j = i + 1; j < nums.length; j++) {
//                 if (nums[i] === nums[j]) {
//                     return true;
//                 }
//             }
//         }
//         return false;
//     }
// }

// learning about the set() function 
// class Solution {
//     /**
//      * @param {number[]} nums
//      * @return {boolean}
//      */
//     hasDuplicate(nums) {
//         const seen = new Set();
//         for (const num of nums) {
//             if (seen.has(num)) {
//                 return true;
//             }
//             seen.add(num);
//         }
//         return false;
//     }
// }

// use properties of set to optimize once more
class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // set has property to remove duplicates, if the new set is shorter than the original list then it had duplicates
        return new Set(nums).size < nums.length;
    }
}

const solution = new Solution();

const test = [1, 2, 3, 3];
const test2 = [1, 2, 3, 4];

console.log(solution.hasDuplicate(test));  // Output: true
console.log(solution.hasDuplicate(test2)); // Output: false