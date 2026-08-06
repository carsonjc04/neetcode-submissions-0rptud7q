class Solution:
    def isHappy(self, n: int) -> bool:
        """
        while n != 1
        str(n)
        cur = n1^2 + n2^2 ...
        add cur to set
        if cur in set:
            return False
        """
        cur = n
        valSet = set()
        while cur != 1:
            curStr = str(cur)
            cur = 0
            for i in curStr:
                cur += int(i) **2
            if cur in valSet:
                return False
            else:
                valSet.add(cur)
        return True