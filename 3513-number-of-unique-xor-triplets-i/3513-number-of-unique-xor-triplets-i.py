class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return n 
        if n == 3:
            return n+1 
        bitCnt = len(bin(n))-2 
        return 2**bitCnt 