class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        prefix = [0 for i in range(len(stones))]
        for i, stone in enumerate(stones):
            if i > 0:
                prefix[i] = prefix[i-1]
            prefix[i] += stone
            
        @cache
        def dfs(i, j, p):
            if i == j and p == 1:
                return 0
            
            if p == 1:
                prev = 0
                if i > 0:
                    prev = prefix[i-1]
                return prefix[j] - prev + dfs(i, j, k)
            
            if i == j:
                return math.inf
            
            if (j - i + 1 - p) % (k-1) :
                return math.inf

            result = math.inf
            # To form arr[i...j] to p piles, we need to form (p-1) piles and 1 pile
            # And then we continue form (p-1) piles as subproblem
            for l in range(i, j):
                result = min(result, dfs(i, l, 1) + dfs(l + 1, j, p - 1))
            return result
        
        result = dfs(0, len(stones) - 1, 1)
        if result == math.inf:
            return -1
        return result