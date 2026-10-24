class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        n = len(s)
        for i in range((n - 1) // 2 + 1):
            if s[i] != s[n - 1 - i]:
                return False
        return True