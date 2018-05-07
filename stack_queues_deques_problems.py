#----------------------IMPLEMENT-STACK-------------------------------

class Stack(object):
    
    def __init__(self):
        self.stk = []
    
    def isEmpty(self):
        return self.stk == 0
        
    def push(self, item):
        self.stk.append(item)
        
    def pop(self):
        return self.stk.pop()
        
    def peek(self):
        return self.stk[len(self.stk)-1]
    
    def size(self):
        return len(self.stk)
    
    
    
#-------------------------------IMPLEMENT-QUEUE-----------------------
        
class Queue(object):
    def __init__(self):
        self.q = []
        
    def isEmpty(self):
        return len(self.q) == 0
    
    def enque(self,item):
        self.q.insert(0, item)
        
    def deque(self):
        return self.q.pop()
        
    def size(self):
        return len(self.q)
    
    
#---------------------------------IMPLEMENT-DEQUE------------------------
    
class Deque(object):
    def __init__(self):
        self.deq = []
        
    def isEmpty(self):
        return self.deq == []
        
    def addFront(self, item):
        self.deq.insert(0, item)
    
    def addRear(self, item):
        self.deq.append(item)
        
    def removeFront(self):
        return self.q.pop(0)
        
    def removeRear(self):
        return self.q.pop()
    
    def size(self):
        return len(self.deq)
    
    
#----------------------------IMPLEMENT-QUEUE-USING-TWO-STACKS------------------
        
# Uses lists instead of your own Stack class.
stack1 = []
stack2 = []

class Queue2Stacks(object):
    
    def __init__(self):  
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        
        self.stack1.append(element)
        self.stack2 = []
        for i in reversed(self.stack1):
            self.stack2.append(i)
    
    def dequeue(self):
        if self.stack2 != []:
            return self.stack2.pop()