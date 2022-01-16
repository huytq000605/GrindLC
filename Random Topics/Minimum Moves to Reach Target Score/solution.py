class Solution:
    def minMoves(self, target: int, doubles: int) -> int:
        if doubles == 0:
            return target - 1
        if target == 1:
            return 0
        else:
            if target % 2 == 0:
                return 1 + self.minMoves(target // 2, doubles - 1)
            else:
                return 2 + self.minMoves((target - 1) // 2, doubles - 1)