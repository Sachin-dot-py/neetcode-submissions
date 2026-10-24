class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = set()
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[left] + nums[right] + nums[i]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    if i != left and i != right:
                        output.add((nums[left], nums[right], nums[i]))
                    left += 1
                    right -= 1
            
        return list(output)