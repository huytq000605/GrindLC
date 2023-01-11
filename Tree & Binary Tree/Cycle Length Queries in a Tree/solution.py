class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []
        for u, v in queries:
            steps = 0
            while u != v:
                if u > v:
                    u //= 2
                else:
                    v //= 2
                steps += 1
            result.append(steps + 1)
        return result
                
