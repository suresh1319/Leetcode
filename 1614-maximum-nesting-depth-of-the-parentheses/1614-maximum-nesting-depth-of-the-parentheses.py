class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        maxAns = float('-inf')
        n = len(s)
        for i in range(n):
            if s[i] == ')':
                cnt -= 1
            if s[i] == '(':
                cnt += 1
            maxAns = max(maxAns,cnt)
        return maxAns