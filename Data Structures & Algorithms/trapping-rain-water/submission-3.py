class Solution:
    def trap(self, height: List[int]) -> int:
        # At each block, the amount of water stored is the min of the max_left and max_right heights. Calculate this for each position and then sum this up for each bar.
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0], max_right[-1] = height[0], height[-1]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        total_water = 0
        for i in range(n):
            total_water += max(min(max_left[i], max_right[i]) - height[i], 0)
        return total_water
            