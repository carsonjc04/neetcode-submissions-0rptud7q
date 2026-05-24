class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encode = ""
        for i in strs:
            encode += str(len(i)) + "#" + i
        return encode
            # = 5#Hello5#World
    def decode(self, s: str) -> List[str]:

        start = 0
        res = []
        while start < len(s):
            j = start
            while s[j] != "#":
                j += 1
            wordlen = int(s[start:j])
            start = j + 1
            res.append(s[start : start + wordlen])
            start = start + wordlen
        return res