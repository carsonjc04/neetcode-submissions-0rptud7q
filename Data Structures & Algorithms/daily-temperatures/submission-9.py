class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        we'll iterate through temp, adding each tmp to stack. check if cur tmp > stack tmp, pop the stack 
        and save that differece between stack index and current index
        [0][0]...
        """
        stack = []
        res = [0] * len(temperatures)
        for i, tmp in enumerate(temperatures):
            while stack and stack[-1][1] < tmp:
                prevInd, prevTmp = stack.pop()
                res[prevInd] = i - prevInd
            stack.append([i, tmp])
        return res
            