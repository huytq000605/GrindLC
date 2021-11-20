class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        
        def binary_search(start, end, value):
            while start < end:
                mid = start + (end - start) // 2
                if arr2[mid] <= value:
                    start = mid + 1
                else:
                    end = mid
            return start
        
        @lru_cache(None)
        def dfs(idx1, idx2, swapPrev):
            if idx1 >= len(arr1):
                return 0
            result = math.inf
            original = arr1[idx1]
            if idx1 > 0:
                if arr1[idx1] <= arr1[idx1 - 1]:
                    idx2 = binary_search(idx2, len(arr2) - 1, arr1[idx1 - 1])
                    if idx2 >= len(arr2) or arr2[idx2] <= arr1[idx1 - 1]: return math.inf
                    arr1[idx1] = arr2[idx2]
                    result = 1 + dfs(idx1 + 1, idx2 + 1, True)
                    arr1[idx1] = original
                else:
                    result = dfs(idx1 + 1, idx2, False)
                    idx2 = binary_search(idx2, len(arr2) - 1, arr1[idx1 - 1])
                    if idx2 < len(arr2) and arr2[idx2] < arr1[idx1]:
                        arr1[idx1] = arr2[idx2]
                        result = min(result, 1 + dfs(idx1 + 1, idx2 + 1, True))
                        arr1[idx1] = original
            else:
                result = dfs(idx1 + 1, idx2, False)
                if arr2[idx2] < arr1[idx1]:
                    arr1[idx1] = arr2[idx2]
                    result = min(result, 1 + dfs(idx1 + 1, idx2 + 1, True))
                    arr1[idx1] = original
            
            return result
        
        ans = dfs(0, 0, False)
        if ans >= math.inf: return -1
        return ans