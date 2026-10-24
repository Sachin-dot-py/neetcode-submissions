class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        chars = set()
        while right < len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length