class Node:
        next = None
        def __init__(self, value):
            self.value = value

class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = Node(value)
    
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        
        currentNode = self.head
        while currentNode:
            if currentNode.value == value:
                return currentNode
            currentNode = currentNode.next
            
        return None
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is not None:
            currentNode = self.head
            if self.head.value == value:
                self.head = self.head.next
            else:
                while currentNode.next:
                    if currentNode.next.value == value:
                        currentNode.next = currentNode.next.next
                        return
                    currentNode = currentNode.next
            
        return
    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        firstNode = None
        if self.head:
            firstNode = self.head
            self.head = self.head.next
        return firstNode.value
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        
        currentNode = self.head
        if pos == 0:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
        else:
            position = 1
            while currentNode.next:
                if position == pos:
                    newNode = Node(value)
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    return
                currentNode = currentNode.next
                position += 1

            if currentNode.next is None:
                currentNode.next = Node(value)
    
    def size(self):
        """ Return the size or length of the linked list. """
        count = 0
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"