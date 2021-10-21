
class Solution:
    def maxSumMinProduct(self, nums):
        res = 0
        stack = []
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1]+num)

        for k,v in enumerate(nums):
            newStart = k
            while stack and stack[-1][1] > v:
                start, val = stack.pop()
                total = prefix[k] - prefix[start]
                res = max(res, total * val)
                newStart = start

            stack.append((newStart, v))

        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res, val*total)

        return res


a = Solution()
print(a.maxSumMinProduct([1,3,2,1,2,3,5,2,1]))