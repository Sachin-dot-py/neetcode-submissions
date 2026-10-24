class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_length = 0
        for num in nums_set:
            # Beginning of the sequence
            if num - 1 not in nums_set:
                curr = num

                while curr + 1 in nums_set:
                    curr += 1
                max_length = max(max_length, curr - num + 1)
        
        return max_length