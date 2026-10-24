class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        max_length = 1
        left = 0
        chars = set(s[0])
        for right in range(1, len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            max_length = max(right - left + 1, max_length)
        return max_length
