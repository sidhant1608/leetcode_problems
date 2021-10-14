def permutationofString(s, curr=""):

    if len(s) == 1:
        return s+curr

    for i in range(len(s)):
        curr = s[i]
        print(permutationofString(s[:-i], curr))

print(permutationofString("abc"))