from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)
        for char in s:
            letters[char] += 1
        for char in t:
            letters[char] -= 1
        for value in letters.values():
            if value != 0:
                return False
        return True