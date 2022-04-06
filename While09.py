def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum_digit=0
    i=0
    while i<len(s):
        if s[i].isdigit():
            sum_digit+=int(s[i])
          
        i+=1    
    return sum_digit
 