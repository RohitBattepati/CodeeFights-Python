def checkPalindrome(inputString):
    if inputString == inputString[::-1]:
        return True
    else:
        return False
		
		
		
# second method

ddef checkPalindrome(inputString):
    left = 0
    right = len(inputString) - 1
    while left < right:
        if inputString[left] != inputString[right]:
            return False
        left += 1
        right -= 1
    return True