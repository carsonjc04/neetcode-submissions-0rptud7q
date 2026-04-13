class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        reversed_ = []
        for i, cnt in count.items():
            reversed_.append([cnt, i])
        reversed_.sort()

        res = []

        while len(res) != k:
            res.append(reversed_.pop()[1])
        return res


