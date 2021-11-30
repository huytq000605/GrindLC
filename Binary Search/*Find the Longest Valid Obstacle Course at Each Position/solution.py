class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        result = []
        states = []
        for height in obstacles:
            if len(states) == 0 or states[-1] <= height:
                states.append(height)
                result.append(len(states))
            else:
                start = 0
                end = len(states) - 1
                while start < end:
                    mid = start + (end - start) // 2
                    if height < states[mid]:
                        end = mid
                    else:
                        start = mid + 1
                states[start] = height
                result.append(start + 1)
        return result