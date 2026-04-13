from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i, strings in enumerate(strs):
            values = ''.join(sorted(strings))
            group[values].append(strings)
        product = list(group.values())
        return product
                