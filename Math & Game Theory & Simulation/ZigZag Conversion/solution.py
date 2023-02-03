class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]
        i, n = 0, len(s)
        m = numRows
        while i < n:
            j = 0
            while i < n and j < m:
                rows[j] += s[i]
                j += 1
                i += 1
            
            j = m-2
            while i < n and j > 0:
                rows[j] += s[i]
                j -= 1
                i += 1
        result = ""
        for row in rows:
            result += row
        return result
                
