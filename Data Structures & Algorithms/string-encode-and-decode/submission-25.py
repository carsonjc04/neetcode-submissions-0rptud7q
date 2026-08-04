class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            j = i + 1
            i = j + length
            res.append(s[j:i])
            j = i
        return res

"""
"5#Hello5#World" -> ["Hello", "World"]
"""