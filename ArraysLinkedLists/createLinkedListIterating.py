class Node:
        next = None
        def __init__(self, value):
            self.value = value

def create_linked_list(elements):
    head = None

    for elem in reversed(elements):
        newNode = Node(elem)
        newNode.next = head
        head = newNode

    return head

def create_linked_list_better(input_list):
    head = None
    tail = None
    for elem in input_list:
        if head == None:
            head = Node(elem)
            tail = head
        else:
            tail.next = Node(elem)
            tail = tail.next
    return head


### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)
           

input_list = [1, 2, 3, 4, 5, 6]


head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)
