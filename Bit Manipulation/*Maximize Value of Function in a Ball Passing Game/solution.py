class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        MAX_BIT = math.ceil(math.log2(k))
        
        # dests[u][bit] = v after 2^bit moves
        dests = [[0 for _ in range(MAX_BIT + 1)] for u in range(n)]
        # s[u][bit] = f(u) after 2^bit moves
        s = [[0 for _ in range(MAX_BIT + 1)] for u in range(n)]

        # move 2^0 = 1
        for u in range(n):
            dests[u][0] = s[u][0] = receiver[u]
        # if u moves 2^0 to v
        # u moves 2^1 means
        # s = u moves 2^0 + v moves 2^0
        # new_v = v moves 2^0
        for i in range(1, MAX_BIT + 1):
            for u in range(n):
                v = dests[u][i-1]
                dests[u][i] = dests[v][i-1]
                s[u][i] = s[u][i-1] + s[v][i-1]

        result = 0
        for start in range(n):
            u = start
            res = start
            for bit in range(MAX_BIT + 1):
                if (k >> bit) & 1 == 0: continue
                res += s[u][bit]
                u = dests[u][bit]
            result = max(res, result)
        return result

                
