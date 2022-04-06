def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    import string
    p=string.punctuation
    count_p=0
    i=0
    while i<len(s):
        if s[i] in p:
            count_p+=1
        i+=1    
    return count_p
   