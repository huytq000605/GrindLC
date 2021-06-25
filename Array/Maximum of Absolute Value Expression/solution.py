class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # |arr1[i] - arr1[j]| + |arr2[i]-arr2[j]| + |i-j|
        # = (arr1[i] + arr2[i] + i) - (arr1[j] + arr2[j] + j)
        # = (arr1[i] - arr2[i] + i) - (arr1[j] - arr2[j] + j)
        # = (-arr1[i] + arr2[i] + i) - (-arr1[j] + arr2[j] + j)
        # = (-arr1[i] - arr2[j] + i) - (-arr1[i] - arr2[j] + j)
        a1 = [arr1[i] + arr2[i] + i for i in range(len(arr1))]
        a2 = [arr1[i] - arr2[i] + i for i in range(len(arr1))]
        a3 = [-arr1[i] + arr2[i] + i for i in range(len(arr1))]
        a4 = [-arr1[i] - arr2[i] + i for i in range(len(arr1))]
        def findAbs(arr: List[int]) -> int:
            minNum = float('inf')
            maxNum = float('-inf')
            for num in arr:
                minNum = min(minNum, num)
                maxNum = max(maxNum, num)
            return maxNum - minNum
        m1, m2, m3, m4 = findAbs(a1), findAbs(a2), findAbs(a3), findAbs(a4)
        return max(m1, m2, m3, m4)