class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        result = 0
        position = dict()
        for i, r in enumerate(row):
            position[r] = i
            
        i = 0
        while i < n:
            value = row[i]
            if value % 2 == 0:
                find = value + 1
            else:
                find = value - 1
            if row[i+1] != find:
                j = position[find]
                position[row[i+1]] = j
                row[i+1], row[j] = row[j], row[i+1]
                result += 1
            i += 2
        return result