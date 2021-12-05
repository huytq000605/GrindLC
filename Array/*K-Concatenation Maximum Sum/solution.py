class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        maxFromStart = 0
        maxFromEnd = 0
        total = 0
        maxSubArray = 0
        n = len(arr)
        MOD = 1e9 + 7
        
        currentMaxSubArray = 0
        for i in range(n):
            total += arr[i]
            maxFromStart = max(maxFromStart, total)
            currentMaxSubArray = max(currentMaxSubArray + arr[i], arr[i])
            maxSubArray = max(maxSubArray, currentMaxSubArray)
            
        tempTotal = 0
        for i in range(n - 1, - 1, -1):
            tempTotal += arr[i]
            maxFromEnd = max(maxFromEnd, tempTotal)
            
        result = max(0, maxSubArray)
        if k > 1:
             result = max(result, total * (k-2) + maxFromStart + maxFromEnd, maxFromStart + maxFromEnd)
                
        return int(result % MOD)