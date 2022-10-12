class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Build topological list for row/col
        def topological(graph, n):
            color = [0 for i in range(n)]
            result = [0 for i in range(n)]
            counter = k - 1

            def dfs(u):
                nonlocal graph, color, counter, result
                color[u] = 1
                for v in graph[u]:
                    if color[v] == 2:
                        continue
                    elif color[v] == 1:
                        return False
                    elif color[v] == 0 and not dfs(v):
                        return False
                result[u] = counter
                counter -= 1
                color[u] = 2
                return True

            for i in range(n):
                if color[i] == 0:
                    if not dfs(i):
                        return []
            return result

        # Input can be duplicated so need to use set
        graph_row = [set() for i in range(k)]
        graph_col = [set() for i in range(k)]
        for u, v in rowConditions:
            graph_row[u-1].add(v-1)
        for u, v in colConditions:
            graph_col[u-1].add(v-1)

        # result as k*k matrix
        result = [[0 for j in range(k)] for i in range(k)]

        # Get topological sorted list
        rows, cols = topological(graph_row, k), topological(graph_col, k)

        # If row/col have cyclic graph
        if not rows or not cols:
            return []

        # Assign row/col independent
        for i in range(k):
            result[rows[i]][cols[i]] = i + 1
        return result
