class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        
        m = len(str1)
        n = len(str2)
        t = [[0 for i in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                
                if i == 0 or j == 0:
                    t[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])

        res = ""
        while m > 0 and n > 0:
            if str1[m-1] == str2[n-1]:
                res = res + str1[m-1]
                m -= 1
                n -= 1
            else:
                if t[m-1][n] > t[m][n-1]:
                    res = res + str1[m-1]
                    m -= 1
                else:
                    res = res + str2[n-1]
                    n -= 1
        while m > 0:
            res = res + str1[m-1]
            m -= 1
        while n > 0:
            res = res + str2[n-1]
            n -= 1
        return res[::-1]
        
a = Solution()
print(a.shortestCommonSupersequence("abcde", "bcdfhg"))