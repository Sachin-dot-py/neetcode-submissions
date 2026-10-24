from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        # Compute freq dict of t
        chars = defaultdict(int)
        for char in t:
            chars[char] += 1

        # Find window in s that matches t
        window = defaultdict(int)
        shortest = (float("-inf"), float("inf"))
        have, need = 0, len(chars)
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1
            if c in chars and window[c] == chars[c]:
                have += 1
            
            while have == need:
                if right - left + 1 < shortest[1] - shortest[0] + 1:
                    shortest = (left, right)
                
                window[s[left]] -= 1
                if s[left] in chars and window[s[left]] < chars[s[left]]:
                    have -= 1
                left += 1

        if shortest == (float("-inf"), float("inf")):
            return ""
        
        return s[shortest[0]: shortest[1] + 1]
