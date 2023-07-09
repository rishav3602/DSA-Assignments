"""
<aside>
💡 **Question 1**

Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than that of the current element. If there does not exist an answer for a position, then make the value ‘-1’.

**Examples:**

```
Input: a[] = [1, 1, 2, 3, 4, 2, 1]
Output : [-1, -1, 1, 2, 2, 1, -1]

Explanation:
Given array a[] = [1, 1, 2, 3, 4, 2, 1]
Frequency of each element is: 3, 3, 2, 1, 1, 2, 3

Lets calls Next Greater Frequency element as NGF
1. For element a[0] = 1 which has a frequency = 3,
   As it has frequency of 3 and no other next element
   has frequency more than 3 so  '-1'
2. For element a[1] = 1 it will be -1 same logic
   like a[0]
3. For element a[2] = 2 which has frequency = 2,
   NGF element is 1 at position = 6  with frequency
   of 3 > 2
4. For element a[3] = 3 which has frequency = 1,
   NGF element is 2 at position = 5 with frequency
   of 2 > 1
5. For element a[4] = 4 which has frequency = 1,
   NGF element is 2 at position = 5 with frequency
   of 2 > 1
6. For element a[5] = 2 which has frequency = 2,
   NGF element is 1 at position = 6 with frequency
   of 3 > 2
7. For element a[6] = 1 there is no element to its
   right, hence -1
```

```
Input : a[] = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
Output : [2, 2, 2, -1, -1, -1, -1, 3, -1, -1]
```

</aside>
"""

def nearest_greater_frequency(arr):
    frequencies = {}
    next_greater_freq = [-1] * len(arr)

    for num in arr:
        frequencies[num] = frequencies.get(num, 0) + 1

    stack = []
    for i, num in enumerate(arr):
        while stack and frequencies[arr[stack[-1]]] < frequencies[num]:
            next_greater_freq[stack.pop()] = num
        stack.append(i)

    return next_greater_freq

# Example usage:
arr = [1, 1, 2, 3, 4, 2, 1]
result = nearest_greater_frequency(arr)
print(result)



"""
<aside>
💡 **Question 2**

Given a stack of integers, sort it in ascending order using another temporary stack.

**Examples:**

```
Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
```

</aside>
"""

def sort_stack(stack):
    temp_stack = []
    while stack:
        temp = stack.pop()
        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())
        temp_stack.append(temp)
    return temp_stack

# Example usage:
stack = [34, 3, 31, 98, 92, 23]
result = sort_stack(stack)
print(result)



"""
<aside>
💡 **Question 3**

Given a stack with **push()**, **pop()**, and **empty()** operations, The task is to delete the **middle** element ****of it without using any additional data structure.

Input  : Stack[] = [1, 2, 3, 4, 5]

Output : Stack[] = [1, 2, 4, 5]

Input  : Stack[] = [1, 2, 3, 4, 5, 6]

Output : Stack[] = [1, 2, 4, 5, 6]

</aside>
"""

def delete_middle(stack, k):
    if k == 1:
        stack.pop()
        return

    temp = stack.pop()
    delete_middle(stack, k - 1)
    stack.append(temp)

# Example usage:
stack = [1, 2, 3, 4, 5]
delete_middle(stack, len(stack) // 2 + 1)
print(stack)



"""
<aside>
💡 **Question 4**

Given a Queue consisting of first **n** natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:

1. Push and pop elements from the stack
2. Pop (Or Dequeue) from the given Queue.
3. Push (Or Enqueue) in the another Queue.

**Examples :**

Input : Queue[] = { 5, 1, 2, 3, 4 } 

Output : Yes 

Pop the first element of the given Queue 

i.e 5. Push 5 into the stack. 

Now, pop all the elements of the given Queue and push them to second Queue. 

Now, pop element 5 in the stack and push it to the second Queue.   

Input : Queue[] = { 5, 1, 2, 6, 3, 4 } 

Output : No 

Push 5 to stack. 

Pop 1, 2 from given Queue and push it to another Queue. 

Pop 6 from given Queue and push to stack. 

Pop 3, 4 from given Queue and push to second Queue. 

Now, from using any of above operation, we cannot push 5 into the second Queue because it is below the 6 in the stack.

</aside>
"""

from queue import Queue
from stack import Stack

def check_queue_arrangement(queue):
    stack = Stack()
    size = queue.qsize()

    for i in range(size):
        curr = queue.get()
        while not stack.isEmpty() and stack.peek() < curr:
            queue.put(stack.pop())
        stack.push(curr)

    while not stack.isEmpty():
        queue.put(stack.pop())

    for i in range(size):
        if queue.queue[i] > queue.queue[i+1]:
            return "No"
    return "Yes"

# Example usage:
queue = Queue()
queue.queue = [5, 1, 2, 3, 4]
result = check_queue_arrangement(queue)
print(result)



"""
<aside>
💡 **Question 5**

Given a number , write a program to reverse this number using stack.

**Examples:**

```
Input : 365
Output : 563

Input : 6899
Output : 9986
```

</aside>
"""

def reverse_number(num):
    stack = []
    while num > 0:
        stack.append(num % 10)
        num //= 10

    reversed_num = 0
    place_value = 1
    while stack:
        reversed_num += stack.pop() * place_value
        place_value *= 10

    return reversed_num

# Example usage:
num = 365
result = reverse_number(num)
print(result)


"""
<aside>
💡 **Question 6**

Given an integer k and a **[queue](https://www.geeksforgeeks.org/queue-data-structure/)** of integers, The task is to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

- **enqueue(x) :** Add an item x to rear of queue
- **dequeue() :** Remove an item from front of queue
- **size() :** Returns number of elements in queue.
- **front() :** Finds front item.
</aside>
"""

from queue import Queue

def reverse_first_k(queue, k):
    if queue.empty() or k <= 0:
        return

    stack = []
    count = 0

    while count < k:
        stack.append(queue.get())
        count += 1

    while stack:
        queue.put(stack.pop())

    for i in range(queue.qsize() - k):
        queue.put(queue.get())

# Example usage:
queue = Queue()
queue.queue = [1, 2, 3, 4, 5]
reverse_first_k(queue, 3)
while not queue.empty():
    print(queue.get(), end=" ")




"""
<aside>
💡 **Question 7**

Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the number of words left in the sequence after this pairwise destruction.

**Examples:**

Input : ab aa aa bcd ab

Output : 3

*As aa, aa destroys each other so,*

*ab bcd ab is the new sequence.*

Input :  tom jerry jerry tom

Output : 0

*As first both jerry will destroy each other.*

*Then sequence will be tom, tom they will also destroy*

*each other. So, the final sequence doesn’t contain any*

*word.*

</aside>
"""

def pairwise_destruction(sequence):
    stack = []
    for word in sequence:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    return len(stack)

# Example usage:
sequence = ['ab', 'aa', 'aa', 'bcd', 'ab']
result = pairwise_destruction(sequence)
print(result)



"""
<aside>
💡 **Question 8**

Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.

**Note:** If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.

**Examples:**

</aside>
"""

def max_absolute_difference(arr):
    left_smaller = [0] * len(arr)
    right_smaller = [0] * len(arr)

    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            right_smaller[stack.pop()] = i
        stack.append(i)

    stack = []
    for i in range(len(arr)-1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            left_smaller[stack.pop()] = i
        stack.append(i)

    max_diff = 0
    for i in range(len(arr)):
        max_diff = max(max_diff, abs(right_smaller[i] - left_smaller[i]) - 1)

    return max_diff

# Example usage:
arr = [2, 4, 8, 7, 7, 9, 3]
result = max_absolute_difference(arr)
print(result)
