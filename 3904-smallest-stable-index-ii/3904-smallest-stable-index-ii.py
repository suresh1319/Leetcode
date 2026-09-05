class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffMin = [-1]*n
        mini = float('inf')
        for i in range(n-1,-1,-1):
            mini = min(mini,nums[i])
            suffMin[i] = mini
        prefMax = float('-inf')
        for i in range(n):
            prefMax = max(prefMax,nums[i])
            score = prefMax-suffMin[i]
            if score<=k:
                return i 
        return -1 