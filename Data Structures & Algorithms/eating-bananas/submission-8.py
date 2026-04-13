class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (r + l) // 2
            cnt = 0
            for i in piles:
                cnt += math.ceil(i / mid)
            if cnt <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res

            