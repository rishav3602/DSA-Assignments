"""
# Assignment Questions 15

<aside>
💡 **Question 1**

Given an array **arr[ ]** of size **N** having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.Next greater element of an element in the array is the nearest element on the right which is greater than the current element.If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

**Example 1:**

```
Input:
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
since it doesn't exist, it is -1.

```

**Example 2:**

```
Input:
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
Explanation:
In the array, the next larger element to
6 is 8, for 8 there is no larger elements
hence it is -1, for 0 it is 1 , for 1 it
is 3 and then for 3 there is no larger
element on right and hence -1.
```

</aside>
"""

def find_next_greater_elements(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        
        stack.append(i)

    return result


"""
<aside>
💡 **Question 2**

Given an array **a** of integers of length **n**, find the nearest smaller number for every element such that the smaller element is on left side.If no small element present on the left print -1.

**Example 1:**

```
Input: n = 3
a = {1, 6, 2}
Output: -1 1 1
Explaination: There is no number at the
left of 1. Smaller number than 6 and 2 is 1.
```

**Example 2:**

```
Input: n = 6
a = {1, 5, 0, 3, 4, 5}
Output: -1 1 -1 0 3 4
Explaination: Upto 3 it is easy to see
the smaller numbers. But for 4 the smaller
numbers are 1, 0 and 3. But among them 3
is closest. Similary for 5 it is 4.
```

</aside>
"""

def find_nearest_smaller_elements(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        
        if stack:
            result[i] = arr[stack[-1]]
        
        stack.append(i)

    return result



"""
<aside>
💡 **Question 3**

Implement a Stack using two queues **q1** and **q2**.

**Example 1:**

```
Input:
push(2)
push(3)
pop()
push(4)
pop()
Output:3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4

```

**Example 2:**

```
Input:
push(2)
pop()
pop()
push(3)
Output:2 -1
```

</aside>
"""

from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.top_element = None

    def push(self, value):
        self.q1.put(value)
        self.top_element = value

    def pop(self):
        if self.isEmpty():
            return -1
        
        while self.q1.qsize() > 1:
            self.top_element = self.q1.get()
            self.q2.put(self.top_element)

        popped_element = self.q1.get()

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return popped_element

    def top(self):
        if self.isEmpty():
            return -1
        return self.top_element

    def isEmpty(self):
        return self.q1.empty()


"""
<aside>
💡 **Question 4**

You are given a stack **St**. You have to reverse the stack using recursion.

**Example 1:**

```
Input:St = {3,2,1,7,6}
Output:{6,7,1,2,3}
```

**Example 2:**

```
Input:St = {4,3,9,6}
Output:{6,9,3,4}
```

</aside>
"""

def reverse_stack(stack):
    if not stack:
        return

    top_element = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top_element)

def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
        return

    top_element = stack.pop()
    insert_at_bottom(stack, element)
    stack.append(top_element)


"""
<aside>
💡 **Question 5**

You are given a string **S**, the task is to reverse the string using stack.

**Example 1:**

```
Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
```

</aside>
"""

def reverse_string(string):
    stack = []
    reversed_string = ""

    for char in string:
        stack.append(char)

    while stack:
        reversed_string += stack.pop()

    return reversed_string

"""
<aside>
💡 **Question 6**

Given string **S** representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like ***, /, + and -**.

**Example 1:**

```
Input: S = "231*+9-"
Output: -4
Explanation:
After solving the given expression,
we have -4 as result.

```

**Example 2:**

```
Input: S = "123+*8-"
Output: -3
Explanation:
After solving the given postfix
expression, we have -3 as result.
```

</aside>
"""

def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            
            stack.append(result)

    return stack[-1]


"""
<aside>
💡 **Question 7**

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**

</aside>
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            top = self.stack.pop()

            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]


"""
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```
"""

def trap(height):
    n = len(height)
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water_trapped = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] > left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1

    return water_trapped
