class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        k = 0
        s = set()
        pairs = set()
        for i in range(n):
            for j in range(i,n):
                pairs.add(nums[i]^nums[j])
        
        for pair in pairs:
            for k in nums:
                s.add(pair^k)
        return len(s)


