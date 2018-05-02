"""
    An empty tree is height-balanced. A non-empty binary tree T is balanced if:
    1) Left subtree of T is balanced
    2) Right subtree of T is balanced
    3) The difference between heights of left subtree and right subtree is not more than 1.
"""
# binary tree node
class Node:
    
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
def height(root):
    if root is None:
        return 0
    
    return 1 + max(height(root.left), height(root.right))
    
def isBalanced(root):
    
    if root is None:
        return 1
        
    lh = height(root.left)
    rh = height(root.right)
    
    if (abs(lh -rh) <= 1 and isBalanced(root.left) and isBalanced(root.right)):
        return 1
    
    return 0
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.left.left = Node(6)

if isBalanced(root):
    print("Tree is balanced")
else :
    print("Tree is not balanced")
    
