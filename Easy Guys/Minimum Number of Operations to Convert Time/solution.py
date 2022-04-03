class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time = int(current[:2]) * 60 + int(current[3:])
        correct_time = int(correct[:2]) * 60 + int(correct[3:])
        result = 0
        diff = correct_time - current_time
        for x in [60, 15, 5, 1]:
            times = diff // x
            diff -= x * times
            result += times
        return result