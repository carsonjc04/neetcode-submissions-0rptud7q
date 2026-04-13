class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = (right + left)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        return -1
