class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if encodedText == "" or rows == 1: return encodedText
        cols = len(encodedText) // rows
        result = ""
        for col in range(cols):
            for position in range(col, len(encodedText), cols + 1):
                result += encodedText[position]
        for i, l in enumerate(result[::-1]):
            if l != " ":
                return result[:len(result) - i]