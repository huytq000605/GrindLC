class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        idx = 0
        result = []
        for a, b, c, m in variables:
            if pow(pow(a, b, 10), c, m) == target:
                result.append(idx)
            idx += 1
        return result
