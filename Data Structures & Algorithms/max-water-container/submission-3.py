class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            max_water = max(max_water, (right - left) * min_height)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return max_water
        