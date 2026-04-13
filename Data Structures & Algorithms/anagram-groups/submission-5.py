class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in range(len(strs)):
            group["".join(sorted(strs[i]))].append(strs[i])
        return list(group.values())