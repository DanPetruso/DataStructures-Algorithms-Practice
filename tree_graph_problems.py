class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val 


#------------------------VALIDATE-BINARY-SEARCH-TREE----------------
def check(node, minval, maxval):
    if node == None:
        return True
    if node.val > maxval or node.val < minval:
        return False
    return check(node.left, minval, node.val) and check(node.right, node.val, maxval)


#-----------------------INORDER-TREE-PRINT------------------------
def inorder(tree):
    while tree != None:
        inorder(tree.left)
        print(tree.val)
        inorder(tree.right)
        
