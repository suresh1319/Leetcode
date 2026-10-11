class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sumOfSquares = 0
        for i in range(n):
            if n%(i+1) == 0:
                sumOfSquares += nums[i]*nums[i]
        return sumOfSquares