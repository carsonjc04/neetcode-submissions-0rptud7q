from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i, string in enumerate(strs):
            sorted_ = ''.join(sorted(string))
            group[sorted_].append(string)
        return list(group.values())
                