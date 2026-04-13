class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        reversed_ = []
        for val, freq in count.items():
            reversed_.append([freq, val])

        reversed_.sort()

        res = []
        while k > 0:
            res.append(reversed_.pop()[1])
            k -= 1
        return res
