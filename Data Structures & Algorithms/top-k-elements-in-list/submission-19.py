class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count the freq of elements
        #sort it from least to most freq. append to list until len(list) == k

        #nums[1,2,2,3,3,3,4,4,4,4], k = 3
        #count[4] = 4
        #count.items() =  [3,3], [4,4], [2,2], [1,1]



        count = Counter(nums)
        
        freqList = []
        for num, cnt in count.items():
            freqList.append([cnt, num])
        
        freqList.sort()

        res = []
        while k > len(res):
            res.append(freqList.pop()[1])
        return res


        
        