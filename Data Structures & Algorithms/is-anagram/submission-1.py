from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)
        for char in s:
            chars[char] += 1
        for char in t:
            chars[char] -= 1
        for char, freq in chars.items():
            if freq != 0:
                return False
        return True