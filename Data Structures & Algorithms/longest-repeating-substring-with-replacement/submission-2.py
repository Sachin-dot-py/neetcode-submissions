class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        count = defaultdict(int)
        for right in range(len(s)):
            count[s[right]] += 1
            substring_length = right - left + 1
            replacements_needed = substring_length - max(count.values())
            while replacements_needed > k:
                count[s[left]] -= 1
                left += 1
                substring_length = right - left + 1
                replacements_needed = substring_length - max(count.values())
            max_length = max(max_length, substring_length)
        return max_length