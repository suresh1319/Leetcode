class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        def compare(a,b):
            if a+b > b+a:
                return -1 
            else:
                return 1
            return 0
        nums = list(map(str,nums))
        nums.sort(key = cmp_to_key(compare))
        ans = "".join(nums)
        return "0" if  ans[0] == "0" else ans