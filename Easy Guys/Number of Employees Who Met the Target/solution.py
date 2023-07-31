class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        result = 0
        for h in hours:
            if h >= target:
                result += 1
        return result
