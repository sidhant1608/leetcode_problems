class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        res = []
        subset = ""
        def dfs(i):
            if i == len(digits):
                res.append(subset)
            for j in dic[digits[i]]:
                subset = subset +  j
                dfs(i+1)
                subset = subset[:-1]
            
            
        
        
        
        dfs(0)
        return res


a = Solution()
print(a.letterCombinations("23"))