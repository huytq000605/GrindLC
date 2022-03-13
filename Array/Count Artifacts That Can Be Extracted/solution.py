class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        cell_to_a = {}
        artifacts_map = defaultdict(int)
        for i, a in enumerate(artifacts):
            r1, c1, r2, c2 = a
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    cell = (r, c)
                    cell_to_a[cell] = i
                    artifacts_map[i] += 1
        result = 0
        for r, c in dig:
            cell = (r, c)
            if cell in cell_to_a:
                artifacts_map[cell_to_a[cell]] -= 1
                if artifacts_map[cell_to_a[cell]] == 0:
                    result += 1
        return result
            