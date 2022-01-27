class Solution:
    def combinationSum(self, candidates, target):
        
        res = []

        def dfs(i, path):
            if sum(path) == target:
                # print(res, path)
                res.append(path.copy())
                return
            
            if sum(path) > target:
                return
            
            for x in range(i, len(candidates)):

                path.append(candidates[x])
                dfs(x, path)
                path.pop()
                
        
        dfs(0, [])
        return res

Solution().combinationSum(
    [2,3,6,7], 7
)