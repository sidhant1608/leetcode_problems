class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)
        print(board)
        
    def backtrack(self,board, r, c):
        
        while board[r][c] != ".":
            c += 1
            if c == 9: c = 0; r += 1
            if r == 9: return True
        for i in range(1, 10):
            board[r][c] = str(i)
            if self.isValidSudoku(board):
                if self.backtrack(board, r, c):
                    return True
            board[r][c] = "."
        return False
            
    
    def isValidSudoku(self, board) -> bool:
    
        return (
            self.is_row_valid(board) and 
            self.is_column_valid(board) and 
            self.is_square_valid(board))
        
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True
    
    def is_column_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
    
    def is_square_valid(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j,j+3)]
                if not self.is_unit_valid(square):
                    return False
        return True
            
    def is_unit_valid(self, unit):
        unit = [x for x in unit if x != "."]
        return len(set(unit)) == len(unit)
        

a = Solution()
# a.solveSudoku(
#     [
#         ["5","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]
#     ]
# )
a.solveSudoku(
    [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]
)
# a.solveSudoku(
#     [
#         ["1",".","."],
#         ["2",".","."],
#         [".",".","1"],
#     ]
# )