class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in range(len(strs)):
            sorted_ = "".join(sorted(strs[i]))
            group[sorted_].append(strs[i])
        return list(group.values())