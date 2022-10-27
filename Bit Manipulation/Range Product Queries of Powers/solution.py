class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = []
        MOD = 10**9 + 7
        result = []
        for i in range(32):
            if (n >> i) & 1:
                arr.append(1 << i)
        for l, r in queries:
            res = 1
            for i in range(l, r +1):
                res *= arr[i]
                res %= MOD
            result.append(res)
        return result
