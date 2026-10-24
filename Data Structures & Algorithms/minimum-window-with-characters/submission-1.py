from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        freq_t = defaultdict(int)
        for char in t:
            freq_t[char] += 1
        
        freq_s = defaultdict(int)
        have, need = 0, len(freq_t)
        result = [-1, -1]
        resultLen = float('inf')
        left = 0
        for right in range(len(s)):
            char = s[right]
            freq_s[char] += 1
            if char in freq_t and freq_t[char] == freq_s[char]:
                have += 1
            
            while have == need:
                if right - left + 1 < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1
                
                freq_s[s[left]] -= 1
                if s[left] in freq_t and freq_s[s[left]] < freq_t[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        return s[left: right + 1] if resultLen != float('inf') else ""