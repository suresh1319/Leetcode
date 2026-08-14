from collections import Counter
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        ans = []
        cnt = 1 
        for i in range(1,n):
            if chars[i] == chars[i-1]:
                cnt += 1 
            else:
                ans.append(chars[i-1]) 
                if cnt>1:
                    ans.extend(str(cnt))
                cnt = 1 
        ans.append(chars[-1])
        if cnt > 1:
            ans.extend(str(cnt))
        chars[:len(ans)] = ans
        return len(ans)