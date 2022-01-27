class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m,n = len(matrix), len(matrix[0])
        res = []
        i,j = 0, 0
        while i < m and j < n:
            print(matrix[i][j], i, j)
            j += 1
            if j == n - 1:
                j == 
        # print(m,n,i,j)

a = Solution()
a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])