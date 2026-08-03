class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        mapp = {}
        for i in range(n):
            if nums[i] in mapp:
                mapp[nums[i]] += 1 
            else:
                mapp[nums[i]] =1 
        for i in range(n):
            rem = k-nums[i]
            if rem == nums[i]:
                if rem in mapp and mapp[rem]>=2:
                    ans += 1
                    mapp[rem] -= 2 
                    if mapp[rem] == 0:
                        del mapp[rem]
            elif rem in mapp and nums[i] in mapp:
                ans += 1
                mapp[rem] -= 1
                mapp[nums[i]] -= 1
                if mapp[rem] == 0:
                    del mapp[rem]
                if mapp[nums[i]] == 0:
                    del mapp[nums[i]] 
        return ans
