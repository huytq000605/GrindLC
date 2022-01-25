class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        up, down = 0, 0
        n = len(arr)
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                return False
            if arr[i] > arr[i-1]:
                if down > 0:
                    return False
                up += 1
            else:
                if up == 0:
                    return False
                down += 1
        return down > 0