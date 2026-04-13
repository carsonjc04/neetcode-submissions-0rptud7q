from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            group[s_sorted].append(s)
        return list(group.values())


                