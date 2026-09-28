class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        n = len(s)
        st = []
        for i in range(n):
            if s[i] == '(':
                st.append("(")
                maxDepth = max(maxDepth,len(st))
            elif s[i] == ")":
                st.pop()
            else:
                continue
        return maxDepth