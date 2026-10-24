class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # skip duplicate triplets
                continue
            # now two sum inside this
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_ == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum_ < 0:
                    l += 1
                else:
                    r -= 1
        return res
            