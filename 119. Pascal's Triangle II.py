class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            row = [1]
            prev = self.getRow(rowIndex - 1)
            for i in range(len(prev) - 1):
                row.append(prev[i] + prev[i+1])
            row.append(1)
            return row
            
a = Solution()
print(a.getRow(3))
