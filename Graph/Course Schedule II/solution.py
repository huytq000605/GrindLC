class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = defaultdict(list)
        for [u, v] in prerequisites:
            req[u].append(v)
        
        result = []
        seen = dict()
        def dfs(course):
            for r in req[course]:
                if r in seen and seen[r] == True:
                    continue
                if r in seen and seen[r] == False:
                    return False
                seen[r] = False
                if not dfs(r):
                    return False
            result.append(course)
            seen[course] = True
            return True
        
        for i in range(numCourses):
            if i in seen:
                continue
            seen[i] = False
            if not dfs(i):
                return []
        
        return result