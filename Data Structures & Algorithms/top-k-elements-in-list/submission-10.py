class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        reversed_count = []
        for value, cnt in count.items():
            reversed_count.append([cnt, value])
        
        reversed_count.sort()
        
        res = []
        while len(res) < k:
            res.append(reversed_count.pop()[1])
        return res


