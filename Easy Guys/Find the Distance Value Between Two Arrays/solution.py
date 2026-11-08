class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        i = 0
        result = 0
        for num in arr1:
            while i < len(arr2) and num - arr2[i] > d:
                i += 1
            if i == len(arr2) or abs(num - arr2[i]) > d:
                result += 1
        return result
