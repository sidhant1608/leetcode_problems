a = [4,1,3,2, 6, 7, 8, 9]

n = len(a)
for i in range(n):
    for j in range(i+1, n+1):
        print(a[i:j])