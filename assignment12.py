"""
<aside>
💡 **Question 1**

Given a singly linked list, delete **middle** of the linked list. For example, if given linked list is 1->2->**3**->4->5 then linked list should be modified to 1->2->4->5.If there are **even** nodes, then there would be **two middle** nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node, then it should return NULL

**Example 1:**

```
Input:
LinkedList: 1->2->3->4->5
Output:1 2 4 5

```

**Example 2:**

```
Input:
LinkedList: 2->4->6->7->5->1
Output:2 4 6 5 1
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteMiddleNode(head):
    if not head or not head.next:
        return None
    
    slow = head
    fast = head
    prev = None
    
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next
    
    return head


"""
<aside>
💡 **Question 2**

Given a linked list of **N** nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
x(position at which tail is connected) = 2
Output:True
Explanation:In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.
```

**Example 2:**

```
Input:
N = 4
value[] = {1,8,3,4}
x = 0
Output:False
Explanation:For N = 4 ,x = 0 means
then lastNode->next = NULL, then
the Linked list does not contains
any loop.
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False



"""
<aside>
💡 **Question 3**

Given a linked list consisting of **L** nodes and given a number **N**. The task is to find the **N**th node from the end of the linked list.

**Example 1:**

```
Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output:8
Explanation:In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 8.

```

**Example 2:**

```
Input:
N = 5
LinkedList: 10->5->100->5
Output:-1
Explanation:In the second example, there
are 4 nodes in the linked list and we
need to find 5th from the end. Since 'n'
is more than the number of nodes in the
linked list, the output is -1.
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getNthFromEnd(head, N):
    if not head or N <= 0:
        return None

    main = head
    ref = head

    # Move ref pointer N nodes ahead
    for _ in range(N):
        if not ref:
            return None
        ref = ref.next

    # If ref pointer reaches the end before N nodes, return None
    if not ref:
        return None

    # Move both pointers until ref reaches the end
    while ref.next:
        main = main.next
        ref = ref.next

    return main.data

   


"""
<aside>
💡 **Question 4**

Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.

!https://media.geeksforgeeks.org/wp-content/uploads/20220816144425/LLdrawio.png

**Examples:**

> Input: R->A->D->A->R->NULL
> 
> 
> **Output:** Yes
> 
> **Input:** C->O->D->E->NULL
> 
> **Output:** No
> 
</aside>
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def isPalindrome(head):
    if not head or not head.next:
        return True

    slow = head
    fast = head

    # Find the middle node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    second_half = reverseLinkedList(slow)
    first_half = head

    # Compare the values of corresponding nodes
    while second_half:
        if first_half.data != second_half.data:
            # Restore the original linked list
            reverseLinkedList(second_half)
            return False
        first_half = first_half.next
        second_half = second_half.next

    # Restore the original linked list
    reverseLinkedList(slow)
    return True


"""
<aside>
💡 **Question 5**

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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeLoop(head):
    if not head or not head.next:
        return head
    
    slow = head
    fast = head

    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # No loop found
    if slow != fast:
        return head

    # Move slow to the head and advance both pointers by one step
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the loop
    fast.next = None

    return head



"""
<aside>
💡 **Question 6**

Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

Difficulty Level: Rookie

**Examples**:

```
Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6

Input:
M = 3, N = 2
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->2->3->6->7->8

Input:
M = 1, N = 1
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->3->5->7->9
```

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndDelete(head, M, N):
    if not head or M <= 0 or N <= 0:
        return head

    curr = head
    count = 1

    while curr:
        if count % M == 0:
            temp = curr
            for _ in range(N):
                if temp.next:
                    temp = temp.next
                else:
                    break
            curr.next = temp.next

        curr = curr.next
        count += 1

    return head



"""
<aside>
💡 **Question 7**

Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtAlternatePositions(first, second):
    if not first:
        return second

    if not second:
        return first

    currFirst = first
    currSecond = second

    while currFirst and currSecond:
        nextFirst = currFirst.next
        nextSecond = currSecond.next

        currFirst.next = currSecond
        currSecond.next = nextFirst

        currFirst = nextFirst
        currSecond = nextSecond

    return first



"""
<aside>
💡 **Question 8**

Given a singly linked list, find if the linked list is [circular](https://www.geeksforgeeks.org/circular-linked-list/amp/) or not.

> A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle. Below is an example of a circular linked list.
> 
</aside>

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isCircular(head):
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
