class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(numbers):
            cur = target - num
            if cur in hashmap:
                return [hashmap[cur], i + 1]
            hashmap[num] = i + 1
        return []
