class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = {}
        mapp[0] = 1
        pref = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            pref += nums[i]
            rem = pref - k
            if rem in mapp:
                ans += mapp[rem]
            mapp[pref] = mapp.get(pref,0)+1
        return ans