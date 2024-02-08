class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = set(num for num in range(1, n**2 + 1))
        repeated = -1
        for r in range(n):
            for c in range(n):
                if grid[r][c] not in nums:
                    repeated = grid[r][c]
                    continue
                nums.remove(grid[r][c])
        
        # repeated + missing + etc = n * (n + 1) / 2
        # repeated - missing + etc = sum(g for g in grid)
        # repeated**2 + missing**2 + etc**2 = n * (n + 1) * (2n + 1) / 6
        # repeated**2 + repeated**2 + etc**2 = sum(g**2 for g in grid)

        return [repeated, list(nums)[0]]
