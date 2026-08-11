class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        prefSum = nums[0] 
        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                prefSum += nums[i]
            else:
                break 
        while prefSum in nums:
            prefSum += 1 
        return prefSum 