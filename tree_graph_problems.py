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
        

#-------------------------TREE-LEVEL-ORDER-PRINT----------------------
import collections

def levelOrderPrint(tree):
    if not tree:
        return None
    nodes = collections.deque([tree])
    
    currCount = 1
    nextCount = 0
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currCount += 1
        print(currentNode.val,)
        
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
            
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
            
        if currCount == 0:
            print('/n')
            currCount = nextCount
            nextCount = 0
    
    
#-----------------------TRIM-BST-----------------------------------
def trimBST(tree,minVal,maxVal):
    if not treee:
        return
    
    tree.left = trimBST(tree.left, minVal, maxVal)
    tree.right = trimBST(tree.right, minVal, maxVal)
    
    if minVal <= tree.val <= maxVal:
        return tree
    
    if minVal > tree.val:
        return tree.right
    
    if maxVal < tree.val:
        return tree.left