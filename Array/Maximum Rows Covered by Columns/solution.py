class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        result = 0
        for chosen in itertools.combinations(range(n), cols):
            covered = 0
            for row in range(m):
                valid = True
                for col in range(n):
                    if mat[row][col] == 1 and col not in chosen:
                        valid = False
                        break
                if valid: covered += 1
            result = max(result, covered)
        return result
