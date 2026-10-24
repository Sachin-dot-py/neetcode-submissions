class Solution:

    def encode(self, strs: List[str]) -> str:
        num_strings = len(strs)
        lengths = []
        for string in strs:
            lengths.append(str(len(string)))
        return f"{num_strings}.{".".join(lengths)}.{".".join(strs)}"

    def decode(self, s: str) -> List[str]:
        parts = s.split(".")
        num_strings = int(parts[0])
        lengths = []
        index = len(parts[0]) + 1
        for part in parts[1:num_strings + 1]:
            lengths.append(int(part))
            index += len(part) + 1
        
        result = []
        for length in lengths:
            result.append(s[index:index+length])
            index += length + 1
        return result
