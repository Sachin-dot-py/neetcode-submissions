class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(substring):
            return substring == substring[::-1]
        
        if len(s) == 1:
            return s
        
        longest_substring = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if j - i + 1 > len(longest_substring) and \
                    check_palindrome(s[i:j+1]):
                    longest_substring = s[i:j+1]
        return longest_substring