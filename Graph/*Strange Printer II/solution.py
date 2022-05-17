from collections import defaultdict

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m  = len(targetGrid)
        n = len(targetGrid[0])
        
        values = set()
        for i in range(m):
            for j in range(n):
                values.add(targetGrid[i][j])
        
        depends = defaultdict(list)
        
		# For each value, print from top left to bottom right
		# If have different value in rectangle => mark depend
        for value in values:
            minRow, minCol = m,n
            maxRow, maxCol = 0, 0
            for i in range(m):
                for j in range(n):
                    if targetGrid[i][j] == value:
                        minRow = min(minRow, i)
                        minCol = min(minCol, j)
                        maxRow = max(maxRow, i)
                        maxCol = max(maxCol, j)
            for i in range(minRow, maxRow + 1):
                for j in range(minCol, maxCol + 1):
                    if targetGrid[i][j] != value:
                        depends[value].append(targetGrid[i][j])    

        def dfs(value):
            nonlocal seen
            for depend in depends[value]:
                if depend in seen:
                    if seen[depend] == False: # Depends on each other => cant print
                        return False
                    continue
                seen[depend] = False
                dfs(depend)
            seen[value] = True # set true for value has been check ok
            return True
        
        seen = dict()
        
        for value in values:
            if value not in seen:
                seen[value] = False
                if not dfs(value):
                    return False

        return True