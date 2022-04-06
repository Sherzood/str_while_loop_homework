def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count_digit=0
    i=0
    while i<len(s):
        if s[i].isdigit():
            count_digit+=1
        i+=1    
    return count_digit
 