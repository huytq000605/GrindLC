class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonal = 0
        result = 0
        for d in dimensions:
            dia = d[0] ** 2 + d[1] ** 2
            if dia > diagonal:
                diagonal = dia
                result = d[0] * d[1]
            elif dia == diagonal:
                result = max(result, d[0] * d[1])
        return result
