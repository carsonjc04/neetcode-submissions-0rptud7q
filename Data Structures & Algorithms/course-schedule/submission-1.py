class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:    
        g = defaultdict(list)

        for a, b in prerequisites:
            g[a].append(b)
        
        VISITED, UNVISITED, VISITING = 2, 0, 1
        states = [UNVISITED] * numCourses

        def dfs(crs):
            if states[crs] == VISITED:
                return True
            if states[crs] == VISITING:
                return False
            states[crs] = VISITING

            for nei in g[crs]:
                if not dfs(nei):
                    return False
            states[crs] = VISITED
            return True
 
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True