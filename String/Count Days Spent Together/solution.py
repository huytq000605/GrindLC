class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def convert(s):
            month, day = int(s[:2]), int(s[3:])
            result = day
            for m in range(month):
                result += days[m]
            return result
            
        alice = (convert(arriveAlice), convert(leaveAlice))
        bob = (convert(arriveBob), convert(leaveBob))
        return max(0, min(alice[1], bob[1]) - max(alice[0], bob[0]) + 1)
