class Solution:
    def lengthOfLongestSubstrings(self, s: str) -> int:
        maxsub = ""
        for i in range(len(s)):
            seen = {}
            seen[s[i]] = True
            sub = s[i]
            for j in range(i+1, len(s), 1):
                if s[j] not in seen:
                    sub += s[j]
                    seen[s[j]] = True
                    
                else:
                    break
            if len(sub) > len(maxsub):
                maxsub = sub
        
        return len(maxsub) 


    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen ={}
        res = 0
        for r in range(len(s)):

            if s[r] not in seen:
                res = max(res, r - l + 1)
            else:
                if seen[s[r]] < l:
                    res = max(res, r - l + 1)
                else:
                    l = seen[s[r]]+1
            seen[s[r]] = r
        return res

        

            
a = Solution()
print(a.lengthOfLongestSubstring("abcdabcerfghbb"))