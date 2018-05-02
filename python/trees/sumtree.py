"""
Check if a given Binary Tree is SumTree
write a function that returns true if the given Binary Tree is SumTree else false. A SumTree is a Binary Tree where the value of a node is equal to sum of the nodes present in its left subtree and right subtree. An empty tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum(root):
    if root is None:
        return 0
    return sum(root.left) + root.data + sum(root.right)

def isSumtree(root):
    #if node is NULL or it's a leaf node then return true
    if root is None or (root.left is None and root.right is None):
        return 1

    #get the sum of nodes in left and right subtrees
    ls = sum(root.left)
    rs = sum(root.right)

    if( (root.data == ls + rs) and isSumtree(root.left) and isSumtree(root.right) ):
        return 1

    return 0


