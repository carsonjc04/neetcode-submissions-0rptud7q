class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_, max_ = 1, max(piles)
        res = max(piles)
        while min_ <= max_:
            mid = (min_ + max_) // 2
            cur = 0
            for i in piles:
                cur += math.ceil(float(i) / mid)
            if cur <= h:
                res = mid
                max_ = mid - 1
            else:
                min_ = mid + 1
        return res
                

            