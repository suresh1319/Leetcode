class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {')':'(',']':'[','}':'{'}
        n = len(s)
        st = []
        if n>=1 and (s[0] == ')' or s[0] == ']' or s[0] == '}'):
            return False
        for i in range(n):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                st.append(s[i])
            else:
                if st and (st[-1] == mapp[s[i]]):
                    st.pop()
                   
                else:
                    return False 
        return len(st) == 0

            
