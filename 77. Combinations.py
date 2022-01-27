class Solution:
    def combine(self, n, k):
        
        res = []
        
        def dfs(path, j):
            if len(path) == k:
                res.append(path)
                return 
            
            if len(path) > k:
                return
            
            for i in range(j, n+1):
                dfs(path+[i], i+1)
        
        dfs([], 1)
        print(res)
            
Solution().combine(
    4, 2
)