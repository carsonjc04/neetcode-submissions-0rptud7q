class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 1

        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for p in piles:
                cur += math.ceil(p / mid)
            if cur > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
            
        return res
            
                