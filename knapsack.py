def knapSack(W, wt, val, n, memo={}):

    key = str(W) + "," + str(n)

    if key in memo:
        return memo[key]
    
    if n == 0 or W == 0:
        return 0

    if wt[n-1] > W:
        memo[key] = knapSack(W, wt, val, n-1, memo)
        return memo[key]

    else:
        memo[key] = (max(
        val[n-1] + knapSack(W-wt[n-1], wt, val, n-1, memo),
        knapSack(W, wt, val, n-1, memo)
        ))
        return memo[key]


#Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))