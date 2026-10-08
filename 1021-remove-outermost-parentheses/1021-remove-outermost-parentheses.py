class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        n = len(s)
        ans = ""
        for i in range(n):
            if s[i] == ')':
                cnt -= 1
            if cnt != 0:
                ans += s[i]
            if s[i] == '(':
                cnt += 1
        return ans