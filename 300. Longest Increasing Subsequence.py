class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)
        
        res = 0
        
        def dfs(i, res, curr):
            if i >= n-1:
                return len(curr)
            else:
                for j in range(i, n):
                    if j == 0 or nums[j] >= curr[-1]:
                        res = max(
                            res,
                            dfs(j+1, res, curr+[nums[j]])
                        )
                    else:
                        res = max(res, dfs(j+1, res, curr[:-1]))
            print(res)
            
            
        dfs(0, res, [])
                    
a = Solution()
a.lengthOfLIS([10,9,2,5,3,7,101,18])