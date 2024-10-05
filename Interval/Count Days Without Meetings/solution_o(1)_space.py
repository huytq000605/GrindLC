class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        cur_end = 1
        result = 0
        for start, end in meetings:
            result += max(0, start - cur_end)
            cur_end = max(end + 1, cur_end)
        return result + max(0, days - cur_end + 1)
