class Solution:
    
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals = sorted(intervals, key=lambda tup: tup[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res
        
                


a = Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))