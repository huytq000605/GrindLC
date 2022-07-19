class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for row in range(2, numRows+1):
            last_row = result[-1]
            current = [1 for i in range(row)]
            for col in range(1, row-1):
                current[col] = last_row[col-1] + last_row[col]
            result.append(current)
        return result
