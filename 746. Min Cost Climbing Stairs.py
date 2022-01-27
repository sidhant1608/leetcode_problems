class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp0= cost[0]
        dp1 = 0
        
        if len(cost) >= 2:
            dp1 = cost[1]
        
        for i in range(2, len(cost)):
            curr = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = curr
            
        return min(dp0, dp1)

a = Solution()
print(a.minCostClimbingStairs([10,15,20]))