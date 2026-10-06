class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        def lowerPos(nums):
            low = 0
            high = len(nums)-1
            ans = -1
            while low<=high:
                mid = low+(high-low)//2
                if nums[mid] == target:
                    ans = mid
                    high = mid - 1
                elif nums[mid]<target:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        def upperPos(nums):
            low = 0
            high = len(nums)-1
            ans = -1
            while low<=high:
                mid = low+(high-low)//2
                if nums[mid] == target:
                    ans = mid
                    low = mid + 1
                elif nums[mid]>target:
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        res = []
        res.append(lowerPos(nums))
        res.append(upperPos(nums))
        return res