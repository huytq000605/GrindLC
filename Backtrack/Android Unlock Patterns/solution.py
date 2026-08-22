
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        mid = [[0 for _ in range(10)] for _ in range(10)]
        mid[1][3] = mid[3][1] = 2
        mid[1][7] = mid[7][1] = 4
        mid[3][9] = mid[9][3] = 6
        mid[7][9] = mid[9][7] = 8
        mid[2][8] = mid[8][2] = mid[3][7] = mid[7][3] = mid[1][9] = mid[9][1] = mid[4][6] = mid[6][4] = 5

        cur = [0 for _ in range(10)]
        def at_most(n, u = 0):
            result = 1
            if sum(cur) == n: return result
            for v in range(1, 10):
                if cur[v]: continue
                if mid[u][v] and not cur[mid[u][v]]: continue
                cur[v] = 1
                result += at_most(n, v)
                cur[v] = 0
            return result

        return at_most(n) - at_most(m-1)
