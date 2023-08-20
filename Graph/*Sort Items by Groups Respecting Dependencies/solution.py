class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = [[] for _ in range(m)]
        for u, g in enumerate(group):
            if g == -1:
                group[u] = m
                m += 1
                groups.append([u])
            else:
                groups[g].append(u)

        before_group = [set() for _ in range(m)]
        before_same_group = [[] for _ in range(n)]
        for u, vs in enumerate(beforeItems):
            ug = group[u]
            for v in vs:
                vg = group[v]
                if ug != vg:
                    before_group[ug].add(vg)
                else:
                    before_same_group[u].append(v)
                    
        def topo(nodes, graph):
            # state == 1: in progress, state = 2: done
            states = defaultdict(int)
            result = []
            def dfs(u):
                if states[u] == 1:
                    return False
                if states[u] == 2:
                    return True
                states[u] = 1
                for v in graph[u]:
                    if not dfs(v):
                        return False
                states[u] = 2
                result.append(u)
                return True
            for u in nodes:
                if states[u] == 0:
                    if not dfs(u): return [], False
            return result, True
        
        order_group, valid = topo([i for i in range(m)], before_group)
        if not valid: return []
        result = []
        for g in order_group:
            order_item, valid = topo(groups[g], before_same_group)
            if not valid: return []
            result.extend(order_item)
                
        return result
        
            
