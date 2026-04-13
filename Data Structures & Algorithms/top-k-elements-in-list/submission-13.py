class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        reversed_ = []
        for val, cnt in count.items():
            reversed_.append([cnt, val])
        reversed_.sort()
        res = []

        while len(res) < k:
            res.append(reversed_.pop()[1])
        return res
        