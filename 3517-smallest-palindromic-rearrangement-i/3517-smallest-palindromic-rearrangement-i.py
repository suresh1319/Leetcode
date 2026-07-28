class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        freq = [0]*26 
        for i in range(n):
            freq[ord(s[i])-ord('a')]+=1
        ans = ""
        mid = ""
        for i in range(26):
            ele = chr(ord('a')+i)
            if freq[i]%2!=0:
                mid = ele 
            cnt = freq[i]//2
            ans += ele*cnt 
        return ans+mid+ans[::-1]