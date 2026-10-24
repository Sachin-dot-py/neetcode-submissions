class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        start = 0
        longest = 0
        for end in range(len(s)):
            while s[end] in chars:
                chars.remove(s[start])
                start += 1
            longest = max(longest, end - start + 1)
            chars.add(s[end])
        return longest
