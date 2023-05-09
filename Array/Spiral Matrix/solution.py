class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])
        mnr, mxr, mnc, mxc = 0, m-1, 0, n-1
        while len(result) < m*n:
            for c in range(mnc, mxc + 1): 
                result.append(matrix[mnr][c])
            mnr += 1
            if len(result) == m*n: return result
            
            for r in range(mnr, mxr + 1):
                result.append(matrix[r][mxc])
            if len(result) == m*n: return result
            mxc -= 1
                
            for c in range(mxc, mnc-1, -1):
                result.append(matrix[mxr][c])
            mxr -= 1
            
            for r in range(mxr, mnr-1, -1):
                result.append(matrix[r][mnc])
            mnc += 1
        return result
    
            
            
