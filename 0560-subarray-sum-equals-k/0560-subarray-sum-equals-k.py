class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mapp = {}
        pref = 0

        cnt = 0
        for i in range(n):
            pref += nums[i]
            if pref == k:
                cnt += 1
            rem = pref - k 
            if rem in mapp:
                cnt += mapp[rem]
            mapp[pref] = mapp.get(pref,0)+1
        return cnt