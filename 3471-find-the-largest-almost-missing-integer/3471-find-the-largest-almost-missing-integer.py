from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)
        if k == 1:
            maxi = float('-inf')
            for key,val in freq.items():
                if val == 1:
                    maxi = max(maxi,key)
            return maxi if maxi != float('-inf') else -1
        elif k == n:
            return max(nums)
        f = nums[0]
        s = nums[n-1]
        fc = 0
        sc = 0
        for i in range(n):
            if nums[i] == f:
                fc += 1
            if nums[i] == s:
                sc += 1 
        if fc == sc == 1:
            return max(f,s)
        if fc == 1:
            return f 
        if sc == 1:
            return s
        return -1 
