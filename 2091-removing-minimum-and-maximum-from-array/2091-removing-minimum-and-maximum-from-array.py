class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        minInd = 0 
        maxInd = 0 
        for i in range(1,n):
            if nums[minInd]>nums[i]:
                minInd = i 
            if nums[maxInd]<nums[i]:
                maxInd = i 
        mini = min(minInd,maxInd)
        maxi = max(maxInd,minInd)
        poss1 = (maxi+1)
        poss2 = n-mini
        poss3 = (mini+1)+(n-maxi)
        return min(poss1,poss2,poss3)
