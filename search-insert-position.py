class Solution:
    def searchInsert(self,nums,target) -> int:
        
        start, end = 0 , len(nums) - 1
        mid = 0

        if target > nums[end]:
            return len(nums)

        if target < nums[start]:
            return start
        
        while start <= end:
            
            mid = (start+end)//2

            if nums[mid] < target:
                if nums[mid+1] <= target:
                    start = mid + 1
                else:
                    return mid + 1
                
            elif nums[mid] > target:
                if nums[mid-1] >= target:
                    end = mid - 1
                else:
                    return mid
                
            else:
                return mid

        
a = Solution()
print(a.searchInsert([1,3,5,6], 7))