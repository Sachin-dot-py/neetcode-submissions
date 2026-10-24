from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = defaultdict(int)
        for char in s1:
            chars[char] += 1
        
        window = defaultdict(int)
        left, right = 0, 0
        while right < len(s2):
            char = s2[right]
            window[char] += 1
            if window == chars:
                return True
            if right - left + 1 >= len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            right += 1
        return False
            