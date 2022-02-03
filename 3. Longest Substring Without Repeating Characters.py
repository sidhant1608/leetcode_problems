class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        
        l, r = 0,0
        res = -2**63
        while l<= r and r < len(s):
            if s[r] in seen:
                l = seen[s[r]] + 1
                r += 1
                res = max(res, r - l)
            else:
                seen[s[r]] = r
                r += 1
                res = max(res, r - l)
        return res

Solution().lengthOfLongestSubstring(
    "abcabcbb"
)