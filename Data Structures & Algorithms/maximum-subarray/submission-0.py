class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = nums[0]
        for r in range(len(nums)):
            curSum += nums[r]
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
        return res