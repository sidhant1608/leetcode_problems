class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            l,r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res

a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))