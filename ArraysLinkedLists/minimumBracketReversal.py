class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0



def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """
    
    stack = Stack()
    closeStack = Stack()
    for char in input_string:
        if char == "{":
            stack.push(char)
        elif char == "}":
            if stack.is_empty():
                closeStack.push(char)
            else:
                stack.pop()

    openStackSize = stack.size()
    closeStackSize = closeStack.size()
    swaps = 0

    if (openStackSize + closeStackSize) % 2 != 0:
        return -1
    if openStackSize == closeStackSize:
        return openStackSize
    elif openStackSize > closeStackSize:
        while stack.size() > closeStack.size():
            closeStack.push(stack.pop())
            swaps += 1
    else:
        while closeStack.size() > stack.size():
            stack.push(closeStack.pop())
            swaps += 1
    return swaps

def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)
    
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]          
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_3)

test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 1]
test_function(test_case_4)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_5)