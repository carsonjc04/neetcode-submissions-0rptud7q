class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for i in strs:
            group["".join(sorted(i))].append(i)
        return list(group.values())