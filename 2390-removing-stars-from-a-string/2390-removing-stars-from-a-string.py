class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        n = len(s)
        for i in range(n):
            if len(s)>0 and s[i] == '*':
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)