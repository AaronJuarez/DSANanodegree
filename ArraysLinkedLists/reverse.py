"""
In this first exercise, the goal is to write a function that takes a string as input and then 
returns the reversed string.

For example, if the input is the string "water", then the output should be "retaw".
"""

def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    
    # TODO: Write your solution here
    stringLenght = len(our_string)
    new_string = ''
    i = stringLenght-1
    while i in range(stringLenght, -1, -1):
        new_string += our_string[i]
        i = i-1
    return new_string

    # Test Cases

print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")