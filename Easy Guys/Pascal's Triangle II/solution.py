class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0 for _ in range(rowIndex + 1)]
        row[0] = 1
        for r in range(1, rowIndex + 1):
            prev = row[0]
            for c in range(1, r+1):
                new_prev = row[c]
                row[c] += prev
                prev = new_prev
        return row
