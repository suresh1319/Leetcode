class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxi = 0
        st = []
        st.append(-1)
        for i,par in enumerate(s):
            if par == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    maxi = max(maxi,i-st[-1])
        return maxi