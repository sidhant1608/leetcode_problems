class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        l,r = 0, n - 1
        area = 0
        while l < r:
            new_area = min(height[l],height[r])*(r - l)
            area = max(area, new_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

a = Solution()
# print(a.maxArea([1,8,6,2,5,4,8,3,7]))
print(a.maxArea([1,2]))