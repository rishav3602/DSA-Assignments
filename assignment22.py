"""
<aside>
💡 Question-1:

Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as in Inorder for the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

Example:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f9dda6ae-60b9-427b-990f-dc5b3117a5e3/Untitled.png)

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def convert_to_dll(root):
    if not root:
        return None
    
    def inorder(node):
        nonlocal prev, head
        
        if not node:
            return
        
        inorder(node.left)
        
        if prev:
            prev.right = node
        else:
            head = node
        
        node.left = prev
        prev = node
        
        inorder(node.right)
    
    prev = None
    head = None
    inorder(root)
    
    return head



"""
<aside>
💡 Question-2

A Given a binary tree, the task is to flip the binary tree towards the right direction that is clockwise. See the below examples to see the transformation.

In the flip operation, the leftmost node becomes the root of the flipped tree and its parent becomes its right child and the right sibling becomes its left child and the same should be done for all left most nodes recursively.

Example1:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5f5bbbe-8607-4f17-9ab4-b31327ffa2d0/Untitled.png)

Example2:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/063636b4-9f35-4524-b6d9-c97e30cac510/Untitled.png)

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def flip_tree(root):
    if not root:
        return None
    
    if not root.left and not root.right:
        return root
    
    flipped_left = flip_tree(root.left)
    flipped_right = flip_tree(root.right)
    
    root.left = None
    root.right = None
    
    if flipped_left:
        root.right = flipped_left
        flipped_left.left = root
    
    if flipped_right:
        flipped_right_leftmost = flipped_right
    
        while flipped_right_leftmost and flipped_right_leftmost.left:
            flipped_right_leftmost = flipped_right_leftmost.left
        
        flipped_right_leftmost.left = root
        root.right = flipped_right
    
    return root



"""
<aside>
💡 Question-3:

Given a binary tree, print all its root-to-leaf paths without using recursion. For example, consider the following Binary Tree.

Input:

        6
     /    \
    3      5
  /   \     \
 2     5     4
     /   \
    7     4

Output:

There are 4 leaves, hence 4 root to leaf paths -
  6->3->2
  6->3->5->7
  6->3->5->4
  6->5>4

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_paths(root):
    if not root:
        return
    
    stack = [(root, str(root.data))]
    
    while stack:
        node, path = stack.pop()
        
        if not node.left and not node.right:
            print(path)
        
        if node.right:
            stack.append((node.right, path + "->" + str(node.right.data)))
        
        if node.left:
            stack.append((node.left, path + "->" + str(node.left.data)))


"""
<aside>
💡 Question-4:

Given Preorder, Inorder and Postorder traversals of some tree. Write a program to check if they all are of the same tree.

**Examples:**

Input : 

        Inorder -> 4 2 5 1 3
        Preorder -> 1 2 4 5 3
        Postorder -> 4 5 2 3 1
Output : 

Yes
Explanation : 

All of the above three traversals are of
the same tree 

                           1
                         /   \
                        2     3
                      /   \
                     4     5

Input : 

        Inorder -> 4 2 5 1 3
        Preorder -> 1 5 4 2 3
        Postorder -> 4 1 2 3 5
Output : 

No

</aside>
"""

def is_same_tree(preorder, inorder, postorder):
    if len(preorder) == len(inorder) == len(postorder) == 0:
        return True
    
    if len(preorder) != len(inorder) or len(preorder) != len(postorder):
        return False
    
    root = preorder[0]
    root_index = inorder.index(root)
    
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]
    
    left_preorder = preorder[1:root_index+1]
    right_preorder = preorder[root_index+1:]
    
    left_postorder = postorder[:root_index]
    right_postorder = postorder[root_index:-1]
    
    return is_same_tree(left_preorder, left_inorder, left_postorder) and \
           is_same_tree(right_preorder, right_inorder, right_postorder)
