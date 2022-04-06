def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count_letters=0
    i=0
    while i<len(s):
        if s[i].isalpha():
            count_letters+=1
        i+=1    
    return count_letters
print(main('sherzod1989'))    