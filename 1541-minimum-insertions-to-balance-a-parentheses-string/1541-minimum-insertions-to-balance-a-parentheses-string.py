class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        st = []
        ans = 0
        i = 0
        while i<n:
            if s[i] == '(':
                st.append('(')
                i+=1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2  # Consume both ')'
                else:
                    ans += 1  # Need a second ')'
                    i += 1
                if st:
                    st.pop()
                else:
                    ans += 1
        ans += len(st)*2
        return ans