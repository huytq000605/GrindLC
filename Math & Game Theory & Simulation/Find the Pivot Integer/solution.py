class Solution:
    def pivotInteger(self, n: int) -> int:
        # x*(x+1) // 2 = n*(n+1)//2 - x*(x+1) // 2 + x
        # x*(x+1) - x = n*(n+1) // 2
        # x^2 = n*(n+1)//2
        total = n*(n+1)//2
        result = int(math.sqrt(total))
        if result * result == total:
            return result
        return -1
        
