class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []
        colors = [0 for _ in range(n)]
        for i, c in queries:
            res = 0
            if result:
                res = result[-1]
                
            if colors[i] != 0 and c != colors[i]:
                if i > 0 and colors[i-1] == colors[i]:
                    res -= 1
                if i < n-1 and colors[i] == colors[i+1]:
                    res -= 1
            
            if c != colors[i]:
                if i > 0 and colors[i-1] == c:
                    res += 1
                if i < n-1 and c == colors[i+1]:
                    res += 1
            
            colors[i] = c
            result.append(res)
        return result
