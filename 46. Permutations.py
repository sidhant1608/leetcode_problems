class Solution:
    def permute(self, nums):
        
        def dfs(nums,path):
            if len(path) == 0:
                res.append(nums)
                return 
            
            for i in nums:
                path.append(i)
                dfs(nums[1:], path)
            path.pop()
        
        res = []
        dfs(nums, [])
        print(res)

        
Solution().permute(
    [1,2,3]
)