def powerset(s, i, curr):

    if i == len(s):
        return [curr]

    return powerset(s, i+1, curr+s[i]) + powerset(s, i+1, curr)

print(powerset("abcd", 0, ""))


