
def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:s   
      a string that is the reverse of input
    """
    
    if len(input) == 0:
        return input
    output = input[-1:] + reverse_string(input[:-1])
    return output


# Test Cases
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")