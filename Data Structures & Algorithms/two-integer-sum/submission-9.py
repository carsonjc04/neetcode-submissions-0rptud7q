class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # key:value
        for i, num in enumerate(nums):
            if target - num in hashmap.keys():
                return [hashmap[target - num], i]
            hashmap[num] = i
        return -1
            
        # target = 7
        # 7 - 3 in hashmap, return 3, hashmap
        # 