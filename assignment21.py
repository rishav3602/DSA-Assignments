"""
<aside>
💡 Question-1

You are given a binary tree. The binary tree is represented using the TreeNode class. Each TreeNode has an integer value and left and right children, represented using the TreeNode class itself. Convert this binary tree into a binary search tree.

Input:

        10

       /   \

     2      7

   /   \

 8      4

Output:

        8

      /   \

    4     10

  /   \

2      7

</aside>
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertToBST(root):
    inorder_vals = []
    inorderTraversal(root, inorder_vals)
    inorder_vals.sort()
    idx = 0
    modifyTree(root, inorder_vals, idx)

def inorderTraversal(node, vals):
    if node is None:
        return
    inorderTraversal(node.left, vals)
    vals.append(node.val)
    inorderTraversal(node.right, vals)

def modifyTree(node, inorder_vals, idx):
    if node is None:
        return
    modifyTree(node.left, inorder_vals, idx)
    node.val = inorder_vals[idx]
    idx += 1
    modifyTree(node.right, inorder_vals, idx)



"""
<aside>
💡 Question-2:

Given a Binary Search Tree with all unique values and two keys. Find the distance between two nodes in BST. The given keys always exist in BST.

Example:

Consider the following BST:

![1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f2455039-7e12-43fc-a7d3-b5be24931c1c/1.png)

**Input-1:**

n = 9

values = [8, 3, 1, 6, 4, 7, 10, 14,13]

node-1 = 6

node-2 = 14

**Output-1:**

The distance between the two keys = 4

**Input-2:**

n = 9

values = [8, 3, 1, 6, 4, 7, 10, 14,13]

node-1 = 3

node-2 = 4

**Output-2:**

The distance between the two keys = 2

</aside>
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDistance(root, node1, node2):
    lca_val = findLCA(root, node1, node2)
    lca = findNode(root, lca_val)
    dist1 = findDistanceFromNode(lca, node1, 0)
    dist2 = findDistanceFromNode(lca, node2, 0)
    return dist1 + dist2

def findLCA(root, node1, node2):
    if root is None:
        return None
    if root.val > node1 and root.val > node2:
        return findLCA(root.left, node1, node2)
    elif root.val < node1 and root.val < node2:
        return findLCA(root.right, node1, node2)
    else:
        return root.val

def findNode(root, val):
    if root is None or root.val == val:
        return root
    if root.val > val:
        return findNode(root.left, val)
    return findNode(root.right, val)

def findDistanceFromNode(node, val, dist):
    if node is None:
        return -1
    if node.val == val:
        return dist
    if node.val > val:
        return findDistanceFromNode(node.left, val, dist + 1)
    return findDistanceFromNode(node.right, val, dist + 1)



"""
<aside>
💡 Question-3:

Write a program to convert a binary tree to a doubly linked list.

Input:

        10

       /   \

     5     20

           /   \

        30     35

Output:

5 10 30 20 35

</aside>

<aside>
💡 Question-4:

Write a program to connect nodes at the same level.

Input:

        1

      /   \

    2      3

  /   \   /   \

4     5 6    7

Output:

1 → -1

2 → 3

3 → -1

4 → 5

5 → 6

6 → 7

7 → -1

</aside>
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertToDLL(root):
    if root is None:
        return None
    
    dummy = TreeNode()
    prev = dummy

    def inorderTraversal(node):
        nonlocal prev
        if node is None:
            return

        inorderTraversal(node.left)

        prev.right = node
        node.left = prev
        prev = node

        inorderTraversal(node.right)

    inorderTraversal(root)

    head = dummy.right
    head.left = None

    return head
