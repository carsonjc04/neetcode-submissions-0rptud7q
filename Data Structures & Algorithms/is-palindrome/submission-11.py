class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Preprocess s to get rid of the spaces and capitals
        # check if s == reversed(s)
        preClean = ""
        for i in s:
            if i.isalnum():
                preClean += i.lower()
        
        return preClean == preClean[::-1]