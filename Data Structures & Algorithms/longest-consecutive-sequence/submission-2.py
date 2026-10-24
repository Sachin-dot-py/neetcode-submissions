class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        for num in nums:
            # only start at start of sequence
            if num - 1 not in set_nums:
                length = 0
                while num in set_nums:
                    length += 1
                    num += 1
                max_length = max(max_length, length)
        return max_length
