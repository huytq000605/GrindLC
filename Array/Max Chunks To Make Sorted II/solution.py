class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        left_max = [arr[0] for i in range(n)]
        right_min = [arr[-1] for i in range(n)]
        result = 1
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], arr[i])
        
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], arr[i])
        
        for i in range(n-1):
            if left_max[i] <= right_min[i+1]:
                result += 1
        return result
            