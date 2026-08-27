from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        n = len(arr)
        s = set()
        for key,val in freq.items():
            if val in s:
                return False 
            s.add(val)
        return True
