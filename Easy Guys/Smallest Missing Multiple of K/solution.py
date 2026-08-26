class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = [0 for _ in range(101)]
        mx = 0
        for num in nums: 
            seen[num] = 1
            mx = max(mx, num)
        mul = 1
        while True:
            if k*mul > mx or not seen[k*mul]: return k*mul
            mul += 1
