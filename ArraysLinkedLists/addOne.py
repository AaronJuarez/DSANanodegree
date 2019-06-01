#You are given a non-negative number in the form of list elements. For example, the number 123 
# would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form 
# of a new list.

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    index = len(arr)-1
    for index in range(index, -1, -1):
        elem = arr[index]
        elem += 1

        if elem != 10:
            arr[index] = elem
            return arr
        else:
            arr[index] = 0

    if index == 0:
        new_arr = [0 for _ in range(len(arr)+1)]
        new_arr[0] = 1
        return new_arr


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")      

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 9]
solution = [1, 3, 0]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)