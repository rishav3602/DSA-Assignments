"""
<aside>
💡 Question-1:

Given preorder of a binary tree, calculate its **[depth(or height)](https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/)** [starting from depth 0]. The preorder is given as a string with two possible characters.

1. ‘l’ denotes the leaf
2. ‘n’ denotes internal node

The given tree can be seen as a full binary tree where every node has 0 or two children. The two children of a node can ‘n’ or ‘l’ or mix of both.

**Examples :**

Input  : nlnll
Output : 2
Explanation :

!https://media.geeksforgeeks.org/wp-content/uploads/btree1.png

Input  : nlnnlll
Output : 3

!https://media.geeksforgeeks.org/wp-content/uploads/dia2.png

</aside>
"""

def calculate_depth(preorder):
    if not preorder:
        return -1
    
    depth = 0
    stack = []
    
    for char in preorder:
        if char == 'n':
            stack.append(char)
        elif char == 'l':
            while stack and stack[-1] == 'l':
                stack.pop()
            
            if stack:
                stack.pop()
                stack.append('l')
                depth = max(depth, len(stack))
                stack.append('l')
            else:
                stack.append('l')
    
    return depth



"""
<aside>
💡 Question-2:

Given a Binary tree, the task is to print the **left view** of the Binary Tree. The left view of a Binary Tree is a set of leftmost nodes for every level.

**Examples:**

***Input:***

            4

          /   \

        5     2

             /   \

            3     1

           /  \

          6    7

***Output:** 4 5 3 6*

**Explanation:**

!https://media.geeksforgeeks.org/wp-content/cdn-uploads/left-view.png

***Input:***

                    1

                  /   \

                2       3

                 \

                   4

                     \

                        5

                           \

                             6

**Output:** 1 2 4 5 6

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_left_view(root):
    if not root:
        return
    
    queue = [(root, 1)]
    max_level = 0
    
    while queue:
        node, level = queue.pop(0)
        
        if level > max_level:
            print(node.data, end=" ")
            max_level = level
        
        if node.left:
            queue.append((node.left, level + 1))
        
        if node.right:
            queue.append((node.right, level + 1))



"""
<aside>
💡 Question-3:

Given a Binary Tree, print the Right view of it.

The right view of a Binary Tree is a set of nodes visible when the tree is visited from the Right side.

**Examples:**

**Input:**

         1

      /     \

   2         3

/   \       /  \

4     5   6    7

             \

               8

**Output**: 

Right view of the tree is 1 3 7 8

**Input:**

         1

       /

    8

  /

7

**Output**: 

Right view of the tree is 1 8 7

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_right_view(root):
    if not root:
        return
    
    queue = [(root, 1)]
    max_level = 0
    
    while queue:
        node, level = queue.pop(0)
        
        if level > max_level:
            print(node.data, end=" ")
            max_level = level
        
        if node.right:
            queue.append((node.right, level + 1))
        
        if node.left:
            queue.append((node.left, level + 1))



"""
<aside>
💡 Question-4:

Given a Binary Tree, The task is to print the **bottom view** from left to right. A node **x** is there in output if x is the bottommost node at its horizontal distance. The horizontal distance of the left child of a node x is equal to a horizontal distance of x minus 1, and that of a right child is the horizontal distance of x plus 1.

**Examples:**

**Input:**

             20

           /     \

        8         22

    /      \         \

5         3        25

        /    \

   10       14

**Output:** 5, 10, 3, 14, 25.

**Input:**

             20

           /     \

        8         22

    /      \      /   \

 5         3    4     25

         /    \

     10       14

**Output:**

5 10 4 14 25.

**Explanation:**

If there are multiple bottom-most nodes for a horizontal distance from the root, then print the later one in the level traversal.

**3 and 4** are both the bottom-most nodes at a horizontal distance of 0, we need to print 4.

</aside>
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.horizontal_distance = 0

def print_bottom_view(root):
    if not root:
        return
    
    queue = [root]
    horizontal_distance_map = {}
    
    while queue:
        node = queue.pop(0)
        horizontal_distance = node.horizontal_distance
        
        horizontal_distance_map[horizontal_distance] = node.data
        
        if node.left:
            node.left.horizontal_distance = horizontal_distance - 1
            queue.append(node.left)
        
        if node.right:
            node.right.horizontal_distance = horizontal_distance + 1
            queue.append(node.right)
    
    for distance in sorted(horizontal_distance_map.keys()):
        print(horizontal_distance_map[distance], end=" ")
