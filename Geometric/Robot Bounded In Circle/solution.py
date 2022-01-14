class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_pos = (0, 0)
        d = 0
        
        for time in range(4):
            for i in instructions:
                if i == "L":
                    d = (d-1) + 4
                    d %= 4
                elif i == "R":
                    d += 1
                    d %= 4
                else:
                    cur_pos = (cur_pos[0] + dirs[d][0], cur_pos[1] + dirs[d][1])
        
        if cur_pos == (0, 0):
            return True
        return False