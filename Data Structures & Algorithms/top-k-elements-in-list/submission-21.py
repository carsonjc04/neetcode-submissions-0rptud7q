class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCnt = Counter(nums)
        #list = most freq from hashmap

        freq = []
        for key, value in numCnt.items():
            freq.append([value, key])
        #freq = [3, 2], [3,3], [1,1]
        freq.sort()

        res = []
        while k > 0:
            res.append(freq.pop()[1])
            k -= 1
        return res

