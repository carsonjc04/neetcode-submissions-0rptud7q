class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        
        arr = []
        for key, value in count.items():
            arr.append([value, key])
            arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res