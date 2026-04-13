class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:

        #"4#Hello5#World"
        #iterate through str, when find "#" append s[i+1: j + length], continue

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i = j + 1 + length
        return res



