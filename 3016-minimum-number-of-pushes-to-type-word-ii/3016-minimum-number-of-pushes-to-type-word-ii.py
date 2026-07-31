from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        freq = Counter(word)
        sorted_cnt = sorted(freq.values(),reverse = True)
        ans = 0
        for i in range(len(sorted_cnt)):
            pushes = (i//8)+1
            ans += sorted_cnt[i]*pushes
        return ans