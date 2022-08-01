class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)
        result = 0
        for row in range(n):
            rows[str(grid[row])] += 1
        for col in range(n):
            arr = [0 for i in range(n)]
            for row in range(n):
                arr[row] = grid[row][col]
            key = str(arr)
            if key in rows:
                result += rows[key]
        return result
