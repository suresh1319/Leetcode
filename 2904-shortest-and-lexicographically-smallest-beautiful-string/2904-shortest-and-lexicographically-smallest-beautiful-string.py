class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        st = 0
        minLen = float('inf')
        ans = ""
        cnt = 0
        for i in range(n):
            if s[i] == '1':
                cnt += 1
            while st<n and cnt>k:
                if s[st] == '1':
                    cnt -= 1
                st += 1
            if cnt == k:
                while st<=i and s[st] == '0':
                    st += 1
                curr = s[st:i+1]
                if len(curr)<minLen:
                    minLen = len(curr)
                    ans = curr
                elif len(curr) == minLen and curr<ans:
                    ans = curr
        return ans