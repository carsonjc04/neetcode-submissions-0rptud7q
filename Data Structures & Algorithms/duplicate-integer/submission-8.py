class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCount = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in numsCount:
                return True
            numsCount[nums[i]] += 1
        return False
            