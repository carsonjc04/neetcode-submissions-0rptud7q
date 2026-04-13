class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_height = 0
        while left < right:
            max_height = max(max_height, ((right - left) * min(heights[left], heights[right])))
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return max_height
        



        