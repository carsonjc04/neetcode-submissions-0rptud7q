class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        minHeap = [-s for s in stones]
        res = []
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            v1 = heapq.heappop(minHeap)
            v2 = heapq.heappop(minHeap)
            if v2 > v1:
                heapq.heappush(minHeap, v1 - v2)
        minHeap.append(0)
        return abs(minHeap[0])