class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        result = 0
        n = len(special)
        prev = bottom
        if special[0] != bottom:
            result = special[0] - 1 - bottom + 1
            
        for i in range(n):
            result = max(result, (special[i] - 1) - (prev+1) + 1)
            prev = special[i]
        
        result = max(result, top - prev)
        return result