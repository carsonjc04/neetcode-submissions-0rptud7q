class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        for key, value in count.items():
            if value < 2:
                return key
        return False