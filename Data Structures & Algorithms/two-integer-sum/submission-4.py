class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity:
        # Space Complexity:
        # High-level: sort nums, use two pointers approach
        # left starts at 0 and right starts at len(nums) - 1
        # increment left if sum < target
        # decrement right if sum > target
        # return when sum == target
        nums_sorted = [(num, i) for i, num in enumerate(nums)]
        nums_sorted.sort() # O(nlogn)
        left, right = 0, len(nums) - 1

        while left < right:
            current = nums_sorted[left][0] + nums_sorted[right][0]
            if current < target:
                left += 1
            elif current == target:
                smaller = min(nums_sorted[left][1], nums_sorted[right][1])
                larger = max(nums_sorted[left][1], nums_sorted[right][1])
                return [smaller, larger]
            else:
                right -= 1