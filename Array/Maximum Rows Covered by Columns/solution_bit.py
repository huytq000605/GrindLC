class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        result = 0
        for bit in range(1 << n):
            set_bit = 0
            for i in range(n):
                if (bit >> i) & 1:
                    set_bit += 1
            if set_bit != cols:
                continue

            covered = 0
            for r in range(m):
                valid = True
                for c in range(n):
                    if mat[r][c] == 1 and not (bit >> c) & 1:
                        valid = False
                        break
                if valid:
                    covered += 1
            result = max(result, covered)
        return result
