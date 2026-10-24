class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_length = 0
        count = {}
        maxf = 0
        while right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length