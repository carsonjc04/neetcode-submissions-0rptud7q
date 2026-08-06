class Solution:
    def isValid(self, s: str) -> bool:
        """"
        s =([{}])
        stack = ([
        {}
        """
        pairs = {"}" : "{", "]" : "[", ")" : "("}

        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif stack:
                tmp = stack.pop()
                if pairs[c] != tmp:
                    return False
            else:
                return False
        return True if not stack else False
