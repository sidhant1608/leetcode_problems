class Solution:
    def exist(self, board, word):

        def dfs(r,c, i):
            if i == len(word):
                return True

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False

            if (r,c) in seen:
                return False
            
            if board[r][c] == word[i]:
                seen.add((r,c))
                res =  (
                    dfs(r+1, c, i+1) or dfs(r-1, c, i + 1)\
                    or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1)
                )
                seen.remove((r,c))
                return res
            else:
                return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if dfs(i, j, 0):
                    return True

# Solution().exist(
#     [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
# )

print(Solution().exist(
    [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"
))