def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count_l=0
    i=0
    while i<len(s):
        if s[i].islower():
            count_l+=1
        i+=1    
    return count_l