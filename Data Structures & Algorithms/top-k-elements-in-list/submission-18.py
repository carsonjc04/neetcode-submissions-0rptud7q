class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        reversed_list = []
        for num, freq in count.items():
            reversed_list.append([freq, num])
        reversed_list.sort()

        res = []
        while len(res) < k:
            res.append(reversed_list.pop()[1])
        return res
