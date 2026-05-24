class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encode = ""
        for i in strs:
            encode += str(len(i)) + "#" + i
        return encode
            # = 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            wordlen = int(s[start:end])
            start = end + 1
            res.append(s[start:start + wordlen])
            start = start + wordlen
        return res


