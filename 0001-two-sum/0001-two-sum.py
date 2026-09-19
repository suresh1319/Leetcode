class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        n = len(nums)
        for i in range(n):
            dict1[nums[i]]=i
        f = -1
        s = -1
        for i in range(n):
            rem = target-nums[i]
            if rem in dict1:
                if i!=dict1[rem]:
                    f = i
                    s = dict1[rem]
        ans = [-1,-1]
        ans[0]=f
        ans[1] = s
        return ans