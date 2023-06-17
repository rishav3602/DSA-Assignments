"""
<aside>
💡 **Question 1**

Given a linked list of **N** nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
X = 2
Output:1
Explanation:The link list looks like
1 -> 3 -> 4
     ^    |
     |____|
A loop is present. If you remove it
successfully, the answer will be 1.

```

**Example 2:**

```
Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output:1
Explanation:The Linked list does not
contains any loop.
```

**Example 3:**

```
Input:
N = 4
value[] = {1,2,3,4}
X = 1
Output:1
Explanation:The link list looks like
1 -> 2 -> 3 -> 4
^              |
|______________|
A loop is present.
If you remove it successfully,
the answer will be 1.
```

</aside>
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectAndRemoveLoop(head):
    slow = head
    fast = head
    
    # Detect the loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # If there is no loop, return the head
    if not fast or not fast.next:
        return head
    
    # Find the start of the loop
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    
    # Remove the loop
    fast.next = None
    
    return head



"""
<aside>
💡 **Question 2**

A number **N** is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

**Example 1:**

```
Input:
LinkedList: 4->5->6
Output:457

```

**Example 2:**

```
Input:
LinkedList: 1->2->3
Output:124
```

</aside>
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addOne(head):
    # Reverse the linked list
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # Add 1 to the reversed linked list
    carry = 1
    curr = prev
    while curr:
        curr.val += carry
        carry = curr.val // 10
        curr.val %= 10
        curr = curr.next
    
    # Reverse the linked list again
    prev = None
    curr = prev
    while prev:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev



"""
<aside>
💡 **Question 3**

Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:(i) a **next** pointer to the next node,(ii) a **bottom** pointer to a linked list where this node is head.Each of the sub-linked-list is in sorted order.Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. **Note:** The flattened list will be printed using the bottom pointer instead of next pointer.

**Example 1:**

```
Input:
5 -> 10 -> 19 -> 28
|     |     |     |
7     20    22   35
|           |     |
8          50    40
|                 |
30               45
Output: 5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every
node in a single level.(Note:| represents the bottom pointer.)

```

**Example 2:**

```
Input:
5 -> 10 -> 19 -> 28
|          |
7          22
|          |
8          50
|
30
Output: 5->7->8->10->19->22->28->30->50
Explanation:
The resultant linked lists has every
node in a single level.

(Note:| represents the bottom pointer.)
```

</aside>
"""

class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def mergeLists(a, b):
    if not a:
        return b
    if not b:
        return a
    
    if a.val <= b.val:
        result = a
        result.next = mergeLists(a.next, b)
    else:
        result = b
        result.next = mergeLists(a, b.next)
    
    result.next.prev = result
    return result

def flatten(head):
    if not head:
        return head
    
    curr = head
    while curr.next:
        curr = curr.next
    
    while curr:
        if curr.child:
            child_tail = curr.child
            while child_tail.next:
                child_tail = child_tail.next
            
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            curr = child_tail
        else:
            curr = curr.prev
    
    return head



"""
<aside>
💡 **Question 4**

You are given a special linked list with **N** nodes where each node has a next pointer pointing to its next node. You are also given **M** random pointers, where you will be given **M** number of pairs denoting two nodes **a** and **b**  **i.e. a->arb = b** (arb is pointer to random node)**.**

Construct a copy of the given list. The copy should consist of exactly **N** new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes **X** and **Y** in the original list, where **X.arb** **-->** **Y**, then for the corresponding two nodes **x** and **y** in the copied list, **x.arb --> y.**

Return the head of the copied linked list.

!https://contribute.geeksforgeeks.org/wp-content/uploads/clone.jpg

**Note** :- The diagram isn't part of any example, it just depicts an example of how the linked list may look like.

**Example 1:**

```
Input:
N = 4, M = 2
value = {1,2,3,4}
pairs = {{1,2},{2,4}}
Output:1
Explanation:In this test case, there
are 4 nodes in linked list.  Among these
4 nodes,  2 nodes have arbitrary pointer
set, rest two nodes have arbitrary pointer
as NULL. Second line tells us the value
of four nodes. The third line gives the
information about arbitrary pointers.
The first node arbitrary pointer is set to
node 2.  The second node arbitrary pointer
is set to node 4.

```

**Example 2:**

```
Input:
N = 4, M = 2
value[] = {1,3,5,9}
pairs[] = {{1,1},{3,4}}
Output:1
Explanation:In the given testcase ,
applying the method as stated in the
above example, the output will be 1.
```

</aside>
"""

class Node:
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None
    
    # Create copies of each node and store mapping in a HashMap
    mapping = {}
    curr = head
    while curr:
        mapping[curr] = Node(curr.val)
        curr = curr.next
    
    # Set next and random pointers of the copied nodes based on the mapping
    curr = head
    while curr:
        copied_node = mapping[curr]
        copied_node.next = mapping.get(curr.next)
        copied_node.random = mapping.get(curr.random)
        curr = curr.next
    
    return mapping[head]



"""
<aside>
💡 **Question 5**

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

**Example 1:**

!https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

```

**Example 2:**

!https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

</aside>
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head
    
    odd_ptr = head
    even_head = head.next
    even_ptr = even_head
    
    while even_ptr and even_ptr.next:
        odd_ptr.next = even_ptr.next
        odd_ptr = odd_ptr.next
        even_ptr.next = odd_ptr.next
        even_ptr = even_ptr.next
    
    odd_ptr.next = even_head
    
    return head



"""
<aside>
💡 **Question 6**

Given a singly linked list of size **N**. The task is to **left-shift** the linked list by **k** nodes, where **k** is a given positive integer smaller than or equal to length of the linked list.

**Example 1:**

```
Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output:8 9 2 4 7
Explanation:Rotate 1:4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

```

**Example 2:**

```
Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output:5 6 7 8 1 2 3 4
```

</aside>
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def leftShift(head, k):
    if not head or not head.next or k == 0:
        return head
    
    # Calculate the length of the linked list
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    # Adjust k if it's larger than the length
    k %= length
    
    if k == 0:
        return head
    
    # Find the (k+1)th node from the end
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    new_head = slow.next
    slow.next = None
    fast.next = head
    
    return new_head



"""
<aside>
💡 **Question 7**

You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**). If the `ith` node does not have a next greater node, set `answer[i] = 0`.

**Example 1:**

!https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext1.jpg

```
Input: head = [2,1,5]
Output: [5,5,0]

```

**Example 2:**

!https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext2.jpg

```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

</aside>
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    if not head:
        return []
    
    result = []
    stack = []
    index = 0
    
    while head:
        result.append(0)
        
        while stack and stack[-1][0] < head.val:
            _, prev_index = stack.pop()
            result[prev_index] = head.val
        
        stack.append((head.val, index))
        index += 1
        head = head.next
    
    return result



"""
<aside>
💡 **Question 8**

Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

**Example 1:**

```
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

```

**Example 2:**

```
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

```

**Example 3:**

</aside>
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    if not head:
        return None
    
    dummy = ListNode(0)
    dummy.next = head
    
    prefix_sum = 0
    prefix_sum_map = {0: dummy}
    curr = dummy
    
    while curr:
        prefix_sum += curr.val
        
        if prefix_sum in prefix_sum_map:
            prev = prefix_sum_map[prefix_sum].next
            temp_sum = prefix_sum + prev.val
            while prev != curr:
                temp_sum += prev.next.val
                del prefix_sum_map[temp_sum]
                prev = prev.next
            
            prefix_sum_map[prefix_sum].next = curr.next
        else:
            prefix_sum_map[prefix_sum] = curr
        
        curr = curr.next
    
    return dummy.next
