class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        res = []
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            first = heapq.heappop(minHeap)
            second = heapq.heappop(minHeap)
            if second > first:
                heapq.heappush(minHeap, first - second)
        minHeap.append(0)
        return abs(minHeap[0])


