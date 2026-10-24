class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string))
            output += "#"
            output += string
        return output

    def decode(self, s: str) -> List[str]:
        strs = []
        index = 0
        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            length = int(s[index:j])
            index = j + 1
            j = index + length
            strs.append(s[index:j])
            index = j
        return strs