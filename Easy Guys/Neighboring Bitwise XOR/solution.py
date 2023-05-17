class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        arr = [0 for _ in range(n)]
        for i in range(n-1):
            if derived[i]:
                arr[i+1] = 1 - arr[i]
            else:
                arr[i+1] = arr[i]
        if derived[-1]:
            if arr[0] == arr[-1]: return False
        else:
            if arr[0] != arr[-1]: return False
        return True
