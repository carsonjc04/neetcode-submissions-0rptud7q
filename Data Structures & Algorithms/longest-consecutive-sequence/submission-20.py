class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach: 
        # nums = [2, 20, 4, 10, 3, 4, 5]
        # Put nums in a set of numbers
        # we start by finding beginning of sequence if nums[i] - 1 not in numSet
        # create len = 1
        # while nums[i] + length in numSet: length += 1. res = max..
        res = 0

        numSet = set(nums)
        for num in nums:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                res = max(res, length)
        return res
        