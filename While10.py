def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum_odd_digits=0
    i=0
    while i<len(s):
        if s[i].isdigit():
            if int(s[i])%2!=0:
                sum_odd_digits+=int(s[i])
        i+=1        
    return sum_odd_digits
