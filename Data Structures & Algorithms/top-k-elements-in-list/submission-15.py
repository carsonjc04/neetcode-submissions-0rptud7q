class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter()
        for i in nums:
            count[i] += 1
        
        tmp = []
        for num, freq in count.items():
            tmp.append([freq, num])
        
        tmp.sort()
        res = []
        while len(res) < k:
            res.append(tmp.pop()[1])
        return res
