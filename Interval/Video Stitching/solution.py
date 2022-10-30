class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda clip: (clip[0], -clip[1]))
        n = len(clips)
        i, end, next_end = 0, 0, 0
        result = 0
        while i < n and clips[i][0] <= end:
            while i < n and clips[i][0] <= end:
                next_end = max(next_end, clips[i][1])
                i += 1
            result += 1
            end = next_end
            if end >= time:
                return result
        return -1
