class Solution:
    def restoreIpAddresses(self, s):
        
        res = []
        
        def dfs(path, n, curr):
            print(path)
            if n < 4 and n > 0:
                path += "."
            if n == 4 and len(path) == len(s) + 3:
                res.append(path)
                return 
            if n > 3:
                return
            
            for i in range(1, 4):
                
                if i <= len(curr):
                    tmp = int(curr[:i])
                    tmp1 = curr[:i]
                    
                    
                    if tmp >= 0 and tmp <= 255:
                        if tmp > 0 and tmp1[0] == '0':
                            continue
                        dfs(path+curr[:i], n+1, curr[i:])
        dfs("", 0, s)

Solution().restoreIpAddresses(
    "0101023"
)