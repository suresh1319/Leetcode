class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        st = 0
        maxLen = float('-inf')
        n = len(nums)
        zeros = 0
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            while zeros>k and st<n:
                if nums[st] == 0:
                    zeros -= 1
                st += 1
            maxLen = max(maxLen,i-st+1)
        return maxLen