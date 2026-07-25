class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)

        for a,b in prerequisites:
            g[a].append(b)
        # g[crs] = prerequistes

        visited, visiting = set(), set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            visiting.add(crs)

            for nei in g[crs]:
                if not dfs(nei):
                    return False
                
            visited.add(crs)
            visiting.remove(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True