class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        i, j = 0, -1
        while i < len(arr):
            if arr[i] % 2 == 0:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
        return arr