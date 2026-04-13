class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mapping = {}

        for i in range(len(x)):
            if x[i] not in mapping:
                mapping[x[i]] = y[i]
            
            mapping[x[i]] = max(mapping[x[i]], y[i])

        return -1 if len(mapping) < 3 else sum(sorted(list(mapping.values()))[-3:])