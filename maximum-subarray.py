
class Solution:
    def maxSubArray(self, nums):
            dpss = [0]*len(nums)
            for i,num in enumerate(nums):
                a = dpss[i-1] + num
                b = max(a, num)
                dpss[i] = b
                print(dpss)
            return max(dpss)

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))