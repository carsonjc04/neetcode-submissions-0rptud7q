class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        
        reversed_ = []
        for key, value in counter.items():
            reversed_.append([value, key])
        
        reversed_.sort()
        res = []

        while len(res) < k:
            res.append(reversed_.pop()[1])
        return res