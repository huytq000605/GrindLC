class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for j in range(n)]
        start, end = 0, n-1
        num = 1
        while start <= end:
            for i in range(start, end + 1):
                result[start][i] = num
                num += 1
            
            for i in range(start + 1, end + 1):
                result[i][end] = num
                num += 1
            
            for i in range(end - 1, start - 1, -1):
                result[end][i] = num
                num += 1
            
            for i in range(end - 1, start, -1):
                result[i][start] = num
                num += 1
            start += 1
            end -= 1
        return result