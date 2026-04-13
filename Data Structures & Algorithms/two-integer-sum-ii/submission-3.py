class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numHash = {}

        for i, num in enumerate(numbers):
            if target - num in numHash:
                return [numHash[target - num], i + 1]
            numHash[numbers[i]] = i + 1
        return []