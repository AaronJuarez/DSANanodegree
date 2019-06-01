
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        self.stack = Stack()
        self.transitionStack = Stack()
        
    def size(self):
        return self.stack.size()
        
    def enqueue(self,item):
        self.stack.push(item)
        
    def dequeue(self):
        while self.stack.size() is not 0:
            self.transitionStack.push(self.stack.pop())
        value = self.transitionStack.pop()
        while self.transitionStack.size() is not 0:
            self.stack.push(self.transitionStack.pop())
        return value


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")