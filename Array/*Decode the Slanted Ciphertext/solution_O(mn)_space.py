class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if encodedText == "" or rows == 1: return encodedText
        cols = len(encodedText) // rows
        grid = [[encodedText[cols * i + j] for j in range(cols)] for i in range(rows)]
        result = ""
        row = 0
        col = 0
        while col < cols:
            i = row
            j = col
            while i < rows and j < cols:
                result += grid[i][j]
                i += 1
                j += 1
            col += 1
        for i, l in enumerate(result[::-1]):
            if l != " ":
                return result[:len(result) - i]