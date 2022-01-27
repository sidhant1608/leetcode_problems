from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = defaultdict(int)
        for x in nums:
            if x in dic:
                dic[x] += 1
            else: 
                dic[x] = 1
        # arr = ([0]*dic[0]) + ([1]*dic[1]) + ([2]*dic[2])
        for i in range(len(nums)):
            if dic[0] > 0:
                nums[i] = 0
                dic[0] -= 1
            elif dic[1] > 0:
                nums[i] = 1
                dic[1] -= 1
            else:
                nums[i] = 2
                dic[2] -= 1
        
a = Solution()
print(a.sortColors([2,0,2,1,1,0()]))