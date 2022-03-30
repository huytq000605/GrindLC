class Solution:
    def sortItems(self, n: int, m: int, group: List[int], before_items: List[List[int]]) -> List[int]:
        item_group = [-1 for i in range(n)]
        groups = defaultdict(set) # All items in each group
        before_groups = defaultdict(list) # All groups appear before group[key]
        before_items_same_group = defaultdict(dict) # first key is group, second key is item, value is all values appear before item
        
        for item, group in enumerate(group):
            if group == -1:
                group = m
                m += 1
            item_group[item] = group
        
        for item, befores in enumerate(before_items):
            group = item_group[item]
            for before in befores:
                before_group = item_group[before]
                if group != before_group:
                    before_groups[group].append(before_group)
                else: 
                    if item not in before_items_same_group[group]:
                        before_items_same_group[group][item] = []
                    before_items_same_group[group][item].append(before)
                        
        def topo(graph, nodes, result):
            seen = dict()
            def dfs(node):
                nonlocal result
                if node in seen and seen[node]:
                    return True
                if node in seen and not seen[node]:
                    return False
                seen[node] = False
                if node in graph:
                    for next_node in graph[node]:
                        if not dfs(next_node):
                            return False
                seen[node] = True
                result.append(node)
                return True
            for node in nodes:
                if not dfs(node):
                    return []
            return result
        
        topo_group = topo(before_groups, [i for i in range(m)], [])
        if len(topo_group) == 0:
            return []
        result = []
        for group in topo_group:
            if len(topo(before_items_same_group[group], groups[group], result)) == 0:
                return []
        return result