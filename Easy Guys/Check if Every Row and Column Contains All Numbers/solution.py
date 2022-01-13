class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in range(n):
            have = set()
            for col in range(n):
                have.add(matrix[row][col])
            if len(have) != n:
                return False
        for col in range(n):
            have = set()
            for row in range(n):
                have.add(matrix[row][col])
            if len(have) != n:
                return False
        return True