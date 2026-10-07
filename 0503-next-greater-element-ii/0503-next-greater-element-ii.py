class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        temp = nums + nums
        n = len(nums)
        st = []
        ans = [-1]*n
        for i in range(n-1,-1,-1):
            while st and st[-1]<=nums[i]:
                st.pop()
            st.append(nums[i])
        for i in range(n-1,-1,-1):
            while st and st[-1]<=nums[i]:
                st.pop()
            if st:
                ans[i] = st[-1]
            st.append(nums[i])
        return ans