def checkPalindrome(inputString):
    i = 0
    max = len(inputString) // 2
    while i <= max:
        print(inputString[i], inputString[-i - 1])
        if inputString[i] == inputString[-i - 1]:
            i += 1
        else:
            return False
    return True

checkPalindrome('aabaa')