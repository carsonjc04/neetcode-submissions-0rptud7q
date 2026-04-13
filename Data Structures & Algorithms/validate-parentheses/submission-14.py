class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}" : "{", ")" : "(", "]" : "["}

        stack = []
        for i in s:
            if i in hashmap.values():
                stack.append(i)
            elif stack and i in hashmap.keys() and stack[-1] == hashmap[i]:
                stack.pop()
            else:
                return False
        return True if not stack else False