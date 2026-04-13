class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        set_ = set(nums)
        if len(nums) != len(set_):
            return True
        return False
        