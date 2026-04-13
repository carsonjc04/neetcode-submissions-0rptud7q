class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        reverse_str = newStr[::-1]
        if newStr == reverse_str:
            return True
        return False