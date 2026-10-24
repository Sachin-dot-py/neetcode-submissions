class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search
        # [3,4,5,6,1,2]
        # Either the min is in the left half or right half
        # If it's in the right half then mid > right (exclusive of mid)
        # If it is the midpoint then low > high
        # If it's in the left half then low > mid

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else: # nums[m] > nums[r] so m < min <= r
                l = m + 1

        return nums[l]
                
            