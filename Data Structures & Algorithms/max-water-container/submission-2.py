class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_amount = 0
        while left < right:
            water = (right - left) * min(heights[left], heights[right])
            max_amount = max(max_amount, water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_amount