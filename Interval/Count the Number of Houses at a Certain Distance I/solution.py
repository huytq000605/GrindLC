class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = x-1, y-1
        result = [0 for _ in range(n)]
        for u in range(n):
            for v in range(u+1, n):
                s = min(v-u, abs(u-x) + 1 + abs(y-v), abs(u-y) + 1 + abs(v-x))
                result[s-1] += 2
        return result
                
        
