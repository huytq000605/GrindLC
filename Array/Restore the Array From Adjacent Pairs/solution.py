class Solution:
    def restoreArray(self, adj_pairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for u, v in adj_pairs:
            d[u].append(v)
            d[v].append(u)
        
        num = -1
        for u, v in d.items():
            if len(v) == 1:
                num = u
                break
        
        result = [num]
        while len(result) < len(adj_pairs) + 1:
            for v in d[num]:
                if len(result) >= 2 and v == result[-2]: continue
                result.append(v)
                num = v
                break
        return result
        
