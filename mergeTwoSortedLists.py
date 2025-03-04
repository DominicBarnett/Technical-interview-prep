# Merge Two Sorted Linked Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:



# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []
# Constraints:

# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100

# solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()  # Dummy node to simplify merging

        while list1 and list2:  # Traverse both lists
            if list1.val < list2.val:
                node.next = list1  # Append smaller node
                list1 = list1.next  # Move list1 forward
            else:
                node.next = list2
                list2 = list2.next  # Move list2 forward
            node = node.next  # Move pointer forward

        # Attach the remaining list (if any)
        node.next = list1 or list2  

        return dummy.next  # Return head of merged list
