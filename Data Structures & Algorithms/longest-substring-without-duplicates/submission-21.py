class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "zxyx"
        maxlen = 0
        l, r = 0, 1
        chars = set()
        for r in range(s)
            while s[r] in charSet:
                .remove(s[l])
                l += 1
            add char
            maxlen = max(maxlen, r - l + 1)
        return maxlen
        """
        l = 0
        charSet = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen