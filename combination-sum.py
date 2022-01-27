class Solution:
    def combinationSum(self, candidates, target):
        
        res = []
        def helper(i, path):
            if sum(path) == target:
                res.append(path[:])
                return
                
            if sum(path) > target:
                return 
            
            for x in range(i, len(candidates)):
                
                path.append(candidates[x])
                helper(x,path)
                path.pop()
                
        helper(0,[])
        print(res)
        return res

a = Solution()
print(a.combinationSum([2,3,6,7],7))