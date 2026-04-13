class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #defaultdict - hashmap that you can add key with no values

        # Iterate through strs and sort each str. Use that sorted as a key. If it matches, then append to that hashmap value/list

        group = defaultdict(list)

        for i in strs:
            group["".join(sorted(i))].append(i)
        return list(group.values())