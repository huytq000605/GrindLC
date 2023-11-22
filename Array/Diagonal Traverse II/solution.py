class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        max_d = 0
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diagonals[r+c].append(nums[r][c])
                max_d = max(max_d, r + c)
        
        result = []
        for d in range(max_d+1):
            if d not in diagonals: continue
            result.extend(diagonals[d][::-1])
        return result
