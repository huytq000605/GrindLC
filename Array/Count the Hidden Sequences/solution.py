class Solution:
    def numberOfArrays(self, diffs: List[int], lower: int, upper: int) -> int:
        lowest = 0
        highest = 0
        balance = 0
        for diff in diffs:
            balance += diff
            lowest = min(lowest, balance)
            highest = max(highest, balance)
        return max(0, (upper - highest) - (lower - lowest) + 1)