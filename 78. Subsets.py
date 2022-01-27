class Solution(object):
    def subsets(self, nums):
        res = []
        def dfs(path, i):
            res.append(path)
            
            for j in range(i, len(nums)):
                dfs(path+[nums[j]], j + 1)
        dfs([],0)
        print(res)



a = Solution()
print(a.subsets([1,2,3]))