class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        # lengths
        encoded = ",".join([str(len(s)) for s in strs])
        # separator
        encoded += ";"
        # strings themselves
        encoded += "".join(strs)

        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        decoded = []
        separator_idx = s.find(";")
        lengths = [int(x) for x in s[: separator_idx].split(",")]
        i = separator_idx + 1
        
        for length in lengths:
            decoded.append(s[i: i + length])
            i += length
        
        return decoded
