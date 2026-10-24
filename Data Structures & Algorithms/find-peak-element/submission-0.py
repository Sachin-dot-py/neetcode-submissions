class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))
        l, r = 1, len(nums) - 2
        while l <= r:
            mid = (l + r) // 2
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid - 1
            elif nums[mid - 1] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        