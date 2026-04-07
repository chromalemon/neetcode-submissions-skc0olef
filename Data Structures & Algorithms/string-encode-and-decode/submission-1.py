class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lengths = []
        for string in strs:
            lengths.append(str(len(string)))
        res = ".".join(lengths) + "#" + "".join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        while s[i] != "#":
            i += 1
        lengths = s[:i].split(".")
        j = i+1
        res = []
        for length in lengths:
            res.append(s[j:j+int(length)])
            j += int(length)
        return res
