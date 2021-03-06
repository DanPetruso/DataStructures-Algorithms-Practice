class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

#--------------CYCLE-CHECK--------------------
#Given a singly linked list, write a function which takes in the first node in a singly 
#linked list and returns a boolean indicating if the linked list contains a "cycle".
#A cycle is when a node's next point actually points back to a previous node in the list.
# This is also sometimes known as a circularly linked list.
#You've been given the Linked List Node class code:

def cycle_check(node):
    
    n1 = node
    n2 = node
    
    while n1.nextnode != None and n2.nextnode != None:
        
        n1 = n1.nextnode
        n2 = n2.nextnode.nextnode
        
        if n1 == n2:
            return True
    return False


##------------------Nth-TO-LAST-NODE-----------------------
#Write a function that takes a head node and an integer value n and then returns 
#the nth to last node in the linked list.
    
def nth_to_last_node(n, head):
    l = [head]
    curr = head
    while curr.nextnode != None:
        l.append(curr)
    return l[len(l) - n]



