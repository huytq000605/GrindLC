class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        common = [0 for _ in range(n+1)]
        result = [0 for _ in range(n)]
        res = 0
        for i in range(n):
            common[A[i]] += 1
            if common[A[i]] == 2:
                res += 1 
            common[B[i]] += 1
            if common[B[i]] == 2:
                res += 1
            result[i] = res
        return result
