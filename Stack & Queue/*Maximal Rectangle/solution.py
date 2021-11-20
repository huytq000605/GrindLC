class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        height = [0 for i in range(n)]
        result = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    height[col] += 1
                else:
                    height[col] = 0
            leftSmaller = [-1 for i in range(n)]
            rightSmaller = [n for i in range(n)]
            
            stack = []
            for col in range(n):
                while len(stack) and height[col] < height[stack[-1]]:
                    rightSmaller[stack.pop()] = col
                stack.append(col)
            
            stack = []
            for col in range(n - 1, -1, -1):
                while len(stack) and height[col] < height[stack[-1]]:
                    leftSmaller[stack.pop()] = col
                stack.append(col)
                
            for col in range(n):
                result = max(result, height[col] * ((rightSmaller[col] - 1) - (leftSmaller[col] + 1) + 1))
            
        return result
                
        