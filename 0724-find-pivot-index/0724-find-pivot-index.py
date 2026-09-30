class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        totalSum = sum(nums)
        n = len(nums)
        pref = 0
        for i in range(n):
            pivot = nums[i]
            suff = totalSum - pref - pivot
            if pref == suff:
                return i
            pref += pivot
        return -1