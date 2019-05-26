# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def merge(list1, list2):
    if list1 is not None or list2 is not None:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        newLinkedList = LinkedList(None)
        elemList1 = list1.head
        elemList2 = list2.head

        while elemList1 and elemList2:
            if elemList1.value < elemList2.value:
                newLinkedList.append(elemList1.value)
                elemList1 = elemList1.next
            else:
                newLinkedList.append(elemList2.value)
                elemList2 = elemList2.next

        if elemList1 is None:
            while elemList2:
                newLinkedList.append(elemList2.value)
                elemList2 = elemList2.next
        elif elemList2 is None:
            while elemList1:
                newLinkedList.append(elemList1.value)
                elemList1 = elemList1.next
        return newLinkedList

class NestedLinkedList(LinkedList):
    def flatten(self):
        flatLinkedList = LinkedList(None)
        currentNode = self.head
        while currentNode:
            flatLinkedList = merge(flatLinkedList, currentNode.value)
            currentNode = currentNode.next
        return flatLinkedList


# Merge Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
    
# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next


# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

nested_linked_list = NestedLinkedList(Node(linked_list))

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list.append(second_linked_list)

solution = nested_linked_list.flatten()
node = solution.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next

assert solution == [1,2,3,4,5]