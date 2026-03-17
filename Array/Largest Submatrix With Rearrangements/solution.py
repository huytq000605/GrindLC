class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # heights[i] = (height, column idx)
        heights = [(0, i) for i in range(n)]
        max_area = 0
        
        # The initial solution would be looping through rows and cols sequentially
        # For each row, sort the heights of all columns then calculate
        # That would resulted in time complexity of O(m*n*log(n))
        # This solution optimizes to avoid sorting on every row by
        # Leverage the fact that at first the heights are sorted
        # And the reset columns can be moved to the end of heights
        for row in range(m):
            next_heights = []
            reset_cols = []
            for height, col in heights:
                if matrix[row][col]:
                    next_heights.append((height + 1, col))
                else:
                    reset_cols.append(col)

            for col in reset_cols:
                next_heights.append((0, col))
            heights = next_heights

            for i, (height, _) in enumerate(heights):
                max_area = max(max_area, (i+1) * height)
        return max_area
