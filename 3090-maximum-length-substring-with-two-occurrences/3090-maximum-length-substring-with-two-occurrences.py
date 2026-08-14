class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mapp = {}
        maxLen = float('-inf')
        n = len(s)
        st = 0
        for i in range(n):
            mapp[s[i]] = mapp.get(s[i],0)+1
            while st<n and mapp[s[i]]>2:
                mapp[s[st]] -= 1 
                if mapp[s[st]]  == 0:
                    del mapp[s[st]]
                st+=1 
            maxLen = max(maxLen,i-st+1)
        return maxLen