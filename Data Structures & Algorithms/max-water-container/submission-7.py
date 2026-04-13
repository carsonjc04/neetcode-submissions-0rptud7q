class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0

        while l <= r:
            tmp = min(heights[l], heights[r]) * (r - l)
            area = max(area, tmp)
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        return area