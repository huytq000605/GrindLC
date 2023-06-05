class Solution:
    def checkStraightLine(self, cs: List[List[int]]) -> bool:
        for i in range(2, len(cs)):
            if (cs[i][0] - cs[0][0]) * (cs[1][1] - cs[0][1]) != (cs[1][0] - cs[0][0]) * (cs[i][1] - cs[0][1]):
                return False
        return True
