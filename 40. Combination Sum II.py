class Solution:
    def combinationSum2(self, candidates, target):
        
        res = []
        candidates.sort()
        print(candidates)

        def helper(i, path):

            if sum(path) == target:
                res.append(path[:])
                return 
            
            if sum(path) > target:
                return 

            for j in range(i, len(candidates)):
                
                # if candidates[j-1] != candidates[j]:
                if j > 0 and candidates[j-1] == candidates[j]:
                    continue
                if candidates[j] > target:
                    break
                path.append(candidates[j])
                helper(i+1, path)
                path.pop()
        helper(0, [])
        print(res)

Solution().combinationSum2(
    [10,1,2,7,6,1,5], 8
)
