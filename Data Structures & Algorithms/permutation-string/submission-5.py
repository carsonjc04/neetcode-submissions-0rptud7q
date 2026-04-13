class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter()
        for i in s1:
            count[i] += 1
        need = len(count)
        for i in range(len(s2)):
            count2, cur = Counter(), 0
            for j in range(i, len(s2)):
                count2[s2[j]] += 1
                if count[s2[j]] < count2[s2[j]]:
                    break
                if count[s2[j]] == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False

