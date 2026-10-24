class Solution:

    def encode(self, strs: List[str]) -> str:
        key = "|".join([str(len(string)) for string in strs])
        return key + "--" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 2:
            return []
        end_keys = s.find("--")
        keys = [int(l) for l in s[:end_keys].split("|")]
        strs = []
        curr = end_keys + 2
        for key in keys:
            strs.append(s[curr: curr + key])
            curr += key
        return strs
