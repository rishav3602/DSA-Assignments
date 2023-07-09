"""
<aside>
💡 Question-1

Given a binary tree, your task is to find subtree with maximum sum in tree.

Examples:

Input1 :       

       1

     /   \

   2      3

  / \    / \

4   5  6   7

Output1 : 28

As all the tree elements are positive, the largest subtree sum is equal to sum of all tree elements.

Input2 :

       1

     /    \

  -2      3

  / \    /  \

4   5  -6   2

Output2 : 7

Subtree with largest sum is :

 -2

 / \

4   5

Also, entire tree sum is also 7.

</aside>
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxSubtreeSum(root):
    max_sum = float('-inf')

    def subtreeSum(node):
        nonlocal max_sum
        if node is None:
            return 0

        left_sum = subtreeSum(node.left)
        right_sum = subtreeSum(node.right)
        curr_sum = node.val + left_sum + right_sum

        max_sum = max(max_sum, curr_sum)

        return curr_sum

    subtreeSum(root)

    return max_sum



"""
<aside>
💡 Question-2

Construct the BST (Binary Search Tree) from its given level order traversal.

Example:

Input: arr[] = {7, 4, 12, 3, 6, 8, 1, 5, 10}

Output: BST:

            7

         /    \

       4     12

     /  \     /

    3   6  8

   /    /     \

 1    5      10

</aside>
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBST(levelorder):
    if not levelorder:
        return None

    root = TreeNode(levelorder[0])
    queue = [root]
    i = 1

    while i < len(levelorder):
        curr_node = queue.pop(0)

        if i < len(levelorder) and levelorder[i] < curr_node.val:
            curr_node.left = TreeNode(levelorder[i])
            queue.append(curr_node.left)
            i += 1

        if i < len(levelorder) and levelorder[i] > curr_node.val:
            curr_node.right = TreeNode(levelorder[i])
            queue.append(curr_node.right)
            i += 1

    return root


"""
<aside>
💡 Question-3

Given an array of size n. The problem is to check whether the given array can represent the level order traversal of a Binary Search Tree or not.

Examples:

Input1 : arr[] = {7, 4, 12, 3, 6, 8, 1, 5, 10}

Output1 : Yes

For the given arr[], the Binary Search Tree is:

            7

         /    \

       4     12

     /  \     /

    3   6  8

   /    /     \

 1    5      10

Input2 : arr[] = {11, 6, 13, 5, 12, 10}

Output2 : No

The given arr[] does not represent the level order traversal of a BST.

</aside>
"""

def isLevelOrderBST(levelorder):
    n = len(levelorder)

    if n <= 1:
        return True

    i = 1
    while i < n and levelorder[i] < levelorder[0]:
        i += 1

    for j in range(i, n):
        if levelorder[j] < levelorder[0]:
            return False

    left_subtree = True
    if i > 1:
        left_subtree = isLevelOrderBST(levelorder[1:i])

    right_subtree = True
    if i < n:
        right_subtree = isLevelOrderBST(levelorder[i:])

    return left_subtree and right_subtree
