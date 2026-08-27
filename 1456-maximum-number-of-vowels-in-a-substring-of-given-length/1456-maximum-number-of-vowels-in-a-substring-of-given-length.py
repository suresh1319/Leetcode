class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        st = 0
        n = len(s)
        vowels = 'aeiou'
        cnt = 0
        maxLen = 0
        for i in range(n):
            if s[i] in vowels:
                cnt += 1
            if st<n and (i-st+1)>k:
                if s[st] in vowels:
                    cnt -= 1
                st += 1
            maxLen = max(maxLen,cnt)
        return maxLen 