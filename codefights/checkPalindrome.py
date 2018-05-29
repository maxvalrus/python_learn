def checkPalindrome(inputString):
    i = 0
    max = len(inputString) // 2
    while i <= max:
        if inputString[i] == inputString[-i - 1]:
            i += 1
        else:
            return False
    return True

if __name__ == "__main__":
    print(checkPalindrome('aabaa'))