class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        prefix = [[0 for j in range(n + 1)] for i in range(m + 1)]
        MOD = 10**9 + 7
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prefix[i][j] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i + 1][j + 1]
                if pizza[i][j] == "A":
                    prefix[i][j] += 1
        
        
        @cache
        def cut(startRow, startCol, k):
            if prefix[startRow][startCol] < k:
                return 0
            
            if k == 1:
                return 1
            
            result = 0
            
            for row in range(startRow + 1, m):
                if prefix[startRow][startCol] - prefix[row][startCol] > 0:
                    result += cut(row, startCol, k - 1)
                
            for col in range(startCol + 1, n):
                if prefix[startRow][startCol] - prefix[startRow][col] > 0:
                    result += cut(startRow, col, k - 1)
                
            return result % MOD
        
        return cut(0, 0, k)
            