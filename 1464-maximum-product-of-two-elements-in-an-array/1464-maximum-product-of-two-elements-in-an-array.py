import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hp = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(hp,nums[i])
            if hp and len(hp)>2:
                heapq.heappop(hp)
        return (hp[0]-1)*(hp[1]-1)
