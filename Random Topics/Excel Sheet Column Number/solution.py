class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        n = len(columnTitle) - 1
        for letter in columnTitle:
            result += (ord(letter) - ord('A') + 1) * pow(26, n)
            n -= 1
        return result