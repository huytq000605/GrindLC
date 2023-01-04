class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        j = -1
        result = 0
        for i, fort in enumerate(forts):
            if fort != 0:
                if j != -1 and forts[j] != fort:
                    result = max(result, i - j - 1)
                j = i
                
        return result
                
