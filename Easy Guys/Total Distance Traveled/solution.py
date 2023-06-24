class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        s = 0
        while mainTank:
            result += 10
            mainTank -= 1
            s += 1
            if s == 5 and additionalTank:
                mainTank += 1
                additionalTank -= 1
                s = 0
        return result
