class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i, num in enumerate(numbers):
            temp = target - numbers[i]
            if temp in hashmap:
                return [hashmap[temp], i + 1]
            hashmap[numbers[i]] = i + 1
        return []

