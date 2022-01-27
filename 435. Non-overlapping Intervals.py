class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda tup: tup[0])
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                print(intervals[i], intervals[i-1], intervals[i][0], intervals[i-1][1])
                count += 1
        print(count)

a = Solution()
print(a.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))