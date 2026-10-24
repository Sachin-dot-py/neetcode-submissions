from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            letters = [0] * 26
            for char in string:
                letters[ord(char) - ord('a')] += 1
            anagrams[tuple(letters)].append(string)
        return list(anagrams.values())