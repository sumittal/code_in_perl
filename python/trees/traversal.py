
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def printInorder(root):
    
    if root:
        
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)
        
def printPostorder(root):
    
    if root:
        
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)
        
def printPreorder(root):
    
    if root:
        
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal of binary tree is:\n")
printPreorder(root)
 
print("\nInorder traversal of binary tree is:\n")
printInorder(root)
 
print("\nPostorder traversal of binary tree is:\n")
printPostorder(root)




