class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(m + n) time and O(1) space where m, n are len(s) and len(t)
        s_chars = [0] * 26
        t_chars = [0] * 26

        # Keep track of all the 
        for c in s:
            s_chars[ord(c) - ord('a')] += 1
        for c in t:
            t_chars[ord(c) - ord('a')] += 1

        for i in range(26):
            if s_chars[i] != t_chars[i]:
                return False
        return True