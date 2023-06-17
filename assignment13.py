"""
<aside>
💡 **Question 1**

Given two linked list of the same size, the task is to create a new linked list using those linked lists. The condition is that the greater node among both linked list will be added to the new linked list.

**Examples:**

```
Input: list1 = 5->2->3->8
list2 = 1->7->4->5
Output: New list = 5->7->4->8

Input:list1 = 2->8->9->3
list2 = 5->3->6->4
Output: New list = 5->8->9->4
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    head = None
    tail = None

    while list1 and list2:
        if list1.data > list2.data:
            new_node = Node(list1.data)
            list1 = list1.next
        else:
            new_node = Node(list2.data)
            list2 = list2.next

        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return head



"""
<aside>
💡 **Question 2**

Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.

For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60.

**Example 1:**

```
Input:
LinkedList: 
11->11->11->21->43->43->60
Output:
11->21->43->60
```

**Example 2:**

```
Input:
LinkedList: 
10->12->12->25->25->25->34
Output:
10->12->25->34
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    if not head:
        return head

    current = head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head



"""
<aside>
💡 **Question 3**

Given a linked list of size **N**. The task is to reverse every **k** nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of *k* then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).

**Example 1:**

```
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output:4 2 2 1 8 7 6 5
Explanation:
The first 4 elements 1,2,2,4 are reversed first
and then the next 4 elements 5,6,7,8. Hence, the
resultant linked list is 4->2->2->1->8->7->6->5.

```

**Example 2:**

```
Input:
LinkedList: 1->2->3->4->5
K = 3
Output:3 2 1 5 4
Explanation:
The first 3 elements are 1,2,3 are reversed
first and then elements 4,5 are reversed.Hence,
the resultant linked list is 3->2->1->5->4.
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseKNodes(head, k):
    if not head or k == 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while True:
        count = 0
        current = prev.next
        while current:
            count += 1
            if count % k == 0:
                prev = reverse(prev, current.next)
                current = prev.next
            else:
                current = current.next
            if not current:
                break
        return dummy.next

def reverse(prev, next_node):
    last = prev.next
    current = last.next

    while current != next_node:
        last.next = current.next
        current.next = prev.next
        prev.next = current
        current = last.next

    return last




"""
<aside>
💡 **Question 4**

Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function) in an efficient way. Give the complexity of your algorithm.

**Example:**

```
Inputs:   1->2->3->4->5->6->7->8->9->NULL and k = 3
Output:   3->2->1->4->5->6->9->8->7->NULL.
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteLastOccurrence(head, key):
    if not head:
        return None

    last_occurrence = None
    previous = None
    current = head

    while current:
        if current.data == key:
            last_occurrence = current
        current = current.next

    if not last_occurrence:
        return head

    if last_occurrence == head:
        head = head.next
    else:
        previous = head
        while previous.next != last_occurrence:
            previous = previous.next
        previous.next = last_occurrence.next

    return head



"""
<aside>
💡 **Question 5**

Given a linked list and a key to be deleted. Delete last occurrence of key from linked. The list may have duplicates.

**Examples**:

```
Input:   1->2->3->5->2->10, key = 2
Output:  1->2->3->5->10
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    head = None
    tail = None

    while list1 and list2:
        if list1.data <= list2.data:
            new_node = Node(list1.data)
            list1 = list1.next
        else:
            new_node = Node(list2.data)
            list2 = list2.next

        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return head



"""
<aside>
💡 **Question 6**

Given two sorted linked lists consisting of **N** and **M** nodes respectively. The task is to merge both of the lists (in place) and return the head of the merged list.

**Examples:**

Input: a: 5->10->15, b: 2->3->20

Output: 2->3->5->10->15->20

Input: a: 1->1, b: 2->4

Output: 1->1->2->4

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverseDoublyLinkedList(head):
    if not head or not head.next:
        return head

    current = head
    while current:
        current.prev, current.next = current.next, current.prev
        if not current.prev:
            head = current
        current = current.prev

    return head


"""
<aside>
💡 **Question 7**

Given a **Doubly Linked List**, the task is to reverse the given Doubly Linked List.

**Example:**

```
Original Linked list 10 8 4 2
Reversed Linked list 2 4 8 10
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverseDoublyLinkedList(head):
    if not head or not head.next:
        return head

    current = head
    while current:
        current.prev, current.next = current.next, current.prev
        if not current.prev:
            head = current
        current = current.prev

    return head



"""
<aside>
💡 **Question 8**

Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.

**Example 1:**

```
Input:
LinkedList = 1 <--> 3 <--> 4
x = 3
Output:1 3
Explanation:After deleting the node at
position 3 (position starts from 1),
the linked list will be now as 1->3.

```

**Example 2:**

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteNodeAtPosition(head, position):
    if not head:
        return None

    if position == 1:
        if head.next:
            head.next.prev = None
        return head.next

    current = head
    count = 1
    while current and count != position:
        current = current.next
        count += 1

    if not current:
        return head

    if current.next:
        current.next.prev = current.prev
    current.prev.next = current.next

    return head
