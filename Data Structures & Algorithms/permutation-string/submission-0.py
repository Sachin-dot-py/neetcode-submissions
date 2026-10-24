class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freqs1 = defaultdict(int)
        freqs2 = defaultdict(int)

        for i in range(len(s1)):
            freqs1[s1[i]] += 1
            freqs2[s2[i]] += 1
        
        matches = 0
        for i in range(26):
            char = chr(ord('a')+i)
            matches += 1 if freqs1[char] == freqs2[char] else 0
        
        low = 0
        for high in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            freqs2[s2[high]] += 1
            if freqs1[s2[high]] == freqs2[s2[high]]:
                matches += 1
            elif freqs1[s2[high]] + 1 == freqs2[s2[high]]:
                matches -= 1

            freqs2[s2[low]] -= 1
            if freqs1[s2[low]] == freqs2[s2[low]]:
                matches += 1
            elif freqs1[s2[low]] - 1 == freqs2[s2[low]]:
                matches -= 1
            low += 1
        return matches == 26