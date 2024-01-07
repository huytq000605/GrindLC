class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        decrease = 0
        for battery in batteryPercentages:
            if battery - decrease > 0:
                decrease += 1
        return decrease

