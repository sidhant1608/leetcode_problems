def compress_string(s):
    i = 0
    res = ""
    count = 1
    while i < len(s):
        print(i)
        if i + 1 < len(s):
            if s[i] == s[i+1]:
                count += 1
            else:
                res += s[i] + str(count)
                count = 1
            i += 1
        else:
            res += s[i] + str(count)
            i += 1
    return res


compress_string("aabacbc")