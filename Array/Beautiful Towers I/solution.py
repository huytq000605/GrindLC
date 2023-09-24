class Solution:
    def maximumSumOfHeights(self, mhs: List[int]) -> int:
        n = len(mhs)
        result = 0
        for peak in range(n):
            res = mhs[peak]
            
            mx = mhs[peak]
            for i in range(peak + 1, n):
                res += min(mx, mhs[i])
                mx = min(mx, mhs[i])
            
            mx = mhs[peak]
            for i in reversed(range(peak)):
                res += min(mx, mhs[i])
                mx = min(mx, mhs[i])
            result = max(res, result)
        return result
            
        
                
