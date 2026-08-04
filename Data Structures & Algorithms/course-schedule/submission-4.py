class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        states = [0] * numCourses

        VISITED, VISITING, UNVISITED = 2,1,0

        def cycle(i):
            if states[i] == VISITING:
                return False
            if states[i] == VISITED:
                return True
            
            states[i] = VISITING

            for nei in preMap[i]:
                if not cycle(nei):
                    return False
            states[i] = VISITED
            return True
        
        for i in range(numCourses):
            if not cycle(i):
                return False
        return True

