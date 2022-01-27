class Solution:
    def getLongestSubsequence(self, A , B):
        # code here 
        m = len(A)
        n = len(B)
        
        if m  == 0 or n  == 0:
            return 0
        elif A[m-1]==B[n-1]:
            return 1 + self.getLongestSubsequence(A[:m-1], B[:n-1])
        else:
            return self.getLongestSubsequence(A[:m-1], B) + self.getLongestSubsequence(A, B[:n-1])

a = Solution()
print(a.getLongestSubsequence("AB", "AB"))