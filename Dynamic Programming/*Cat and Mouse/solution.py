class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        @cache
        def dfs(cat, mouse, turn):
            if turn > n * 2:
                return 0
            
            haveDraw = False
            if turn % 2 == 1:
                for nextCat in graph[cat]:
                    if nextCat == 0:
                        continue
                    if nextCat == mouse:
                        return 2
                    thisMove = dfs(nextCat, mouse, turn + 1)
                    if thisMove == 2:
                        return 2
                    elif thisMove == 0:
                        haveDraw = True
                # If it cannot win, it try to draw if possible
                return 0 if haveDraw else 1
            else:
                for nextMouse in graph[mouse]:
                    if nextMouse == cat:
                        continue
                    if nextMouse == 0:
                        return 1
                    thisMove = dfs(cat, nextMouse, turn + 1)
                    if thisMove == 1:
                        return 1
                    elif thisMove == 0:
                        haveDraw = True
                # If it cannot win, it try to draw if possible
                return 0 if haveDraw else 2
            
        return dfs(2, 1, 0)