class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        start = 0
        freq = defaultdict(int)
        freq[s[0]] = 1
        max_freq = 1
        for end in range(1, len(s)):
            freq[s[end]] += 1
            max_freq = max(max_freq, freq[s[end]])
            while (end - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        return res
