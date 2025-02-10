# Minimum Stack
# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in 
# O
# (
# 1
# )
# O(1) time.

# Example 1:

# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# Constraints:

# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.

# solution

class MinStack:
    def __init__(self):
        """
        Initializes the stack.
        - self.min stores the current minimum value in the stack.
        - self.stack stores the elements as differences relative to self.min.
        """
        self.min = float('inf')  # Initial min value
        self.stack = []  # Stack to store transformed values

    def push(self, x: int) -> None:
        """
        Pushes an element onto the stack.
        - If the stack is empty, store 0 and set min to x.
        - Otherwise, store x - self.min to track the difference.
        - If x is smaller than the current min, update self.min.
        """
        if not self.stack:
            self.stack.append(0)  # Placeholder since x is the first element
            self.min = x  # Update min to x
        else:
            self.stack.append(x - self.min)  # Store difference
            if x < self.min:
                self.min = x  # Update min if x is smaller

    def pop(self) -> None:
        """
        Removes the top element from the stack.
        - If the popped value is negative, it means self.min was updated during the push.
        - Restore the previous minimum by subtracting the stored difference.
        """
        if not self.stack:
            return  # No elements to pop

        pop = self.stack.pop()  # Retrieve the stored difference

        if pop < 0:
            self.min = self.min - pop  # Restore the previous minimum

    def top(self) -> int:
        """
        Returns the top element of the stack.
        - If the top value is positive, it represents (x - self.min), so return (top + self.min).
        - If the top value is negative or zero, it means the top was the minimum itself, so return self.min.
        """
        top = self.stack[-1]  # Get the stored difference

        if top > 0:
            return top + self.min  # Retrieve original value
        else:
            return self.min  # If negative, the top was the minimum

    def getMin(self) -> int:
        """
        Returns the minimum element in the stack.
        - Since self.min is always updated correctly, just return it.
        """
        return self.min

