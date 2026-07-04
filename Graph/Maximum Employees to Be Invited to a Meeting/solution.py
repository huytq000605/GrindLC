class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        cycles = []
        depends = defaultdict(set)
        seen = set()
        for cur in range(n):
            depends[favorite[cur]].add(cur)
            if cur not in seen:
                met = {cur: 1}
                while cur not in seen:
                    next_person = favorite[cur]
                    seen.add(cur)
                    if next_person in met:
                        cycles.append([next_person, met[cur] - met[next_person] + 1])
                        break
                    met[next_person] = met[cur] + 1
                    cur = next_person
        
        max_cycle = 0
        cycle_2s = []
        for start, len_cycle in cycles:
            if len_cycle == 2:
                cycle_2s.append(start)
                continue
            max_cycle = max(max_cycle, len_cycle)
        

        def dfs(u, seen):
            result = 0
            for v in depends[u]:
                if v in seen: continue
                seen.add(v)
                result = max(result, 1 + dfs(v, seen))
            return result

        free = 0
        seen = set()
        for u in cycle_2s:
            v = favorite[u]
            seen.add(u)
            seen.add(v)
            a, b = dfs(u, seen), dfs(v, seen)
            free += 2 + a + b
        
        return max(free, max_cycle)
            
       
        
                
                    
