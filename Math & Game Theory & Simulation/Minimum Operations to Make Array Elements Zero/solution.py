
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        times = [1] + [4**n for n in range(1, 16)]
        result = 0
        for s, e in queries:
            i = floor(log(e, 4))
            j = floor(log(s, 4))
            upper = e
            remaining = 0
            res = 0
            for idx in range(i, j-1, -1):
                t = idx + 1
                lower = s if idx == j else times[idx]
                n = upper - lower + 1
                res += n * t
                upper = lower-1
            result += (res + 1) // 2
        return result
