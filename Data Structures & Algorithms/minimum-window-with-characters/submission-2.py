class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = defaultdict(int)
        for char in t:
            t_freq[char] += 1
        
        start = 0
        s_freq = defaultdict(int)
        chars_completed = 0
        res = [-1, -1]
        resLen = float('inf')
        for end in range(len(s)):
            s_freq[s[end]] += 1
            if s[end] in t_freq and s_freq[s[end]] == t_freq[s[end]]:
                chars_completed += 1
            while chars_completed == len(t_freq):
                if end - start + 1 < resLen:
                    res = [start, end]
                    resLen = end - start + 1
                
                s_freq[s[start]] -= 1
                if s[start] in t_freq and s_freq[s[start]] < t_freq[s[start]]:
                    chars_completed -= 1
                start += 1
        substring = s[res[0]: res[1] + 1]
        return substring if resLen != float('inf') else ""