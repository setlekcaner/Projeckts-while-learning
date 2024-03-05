def isIn(char, aStr):
    '''

    char: a single character
    astr: an alphabetized string
     return: True if char is in astr; False otherwise
    '''

    mid = int(len(aStr) / 2)
    mid_str = aStr[mid:mid + 1]
    if len(aStr) == len(char):
        if aStr == char:
            return True
        else:
            return False

    else:
        while char == mid_str:
            return True
        if char > mid_str:
            return isIn(char, aStr[mid:])
        else:
            return isIn(char, aStr[: mid])


print(isIn('u', 'fjmptuuw'))