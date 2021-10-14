def ispalindrome(s, l, r):

    if l >= r:
        return True

    if s[l] != s[r]:
        return False

    return ispalindrome(s, l+1, r-1)


print(ispalindrome("racecar", 0, len("racecar")-1))

        