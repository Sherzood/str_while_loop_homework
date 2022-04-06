def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    cons='a,e,i,o,u,y,A,E,I,O,U,Y'
    count_c=0
    idx=0
    while i<len(s):
        if s[idx].isalpha:
            if s[idx] not in cons:
                count_c+=1
        idx+=1    
    return count_c
  