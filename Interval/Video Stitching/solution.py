class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        i, end = 0, 0
        result = 0
        clips.sort()
        while i < n and clips[i][0] <= end:
            result += 1
            next_end = end
            while i < n and clips[i][0] <= end:
                next_end = max(next_end, clips[i][1])
                i += 1
            end = next_end
            if end >= time:
                break
        if end < time:
            return -1
        return result
