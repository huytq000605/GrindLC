class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        dirs = {
            "L": [0, -1],
            "R": [0, 1],
            "U" : [-1, 0],
            "D": [1, 0]
        }
        result = [0] * len(s)
        for i in range(len(s)):
            cur = [*startPos]
            for j in range(i, len(s)):
                d = dirs[s[j]]
                cur[0] += d[0]
                cur[1] += d[1]
                if cur[0] < 0 or cur[0] >= n or cur[1] < 0 or cur[1] >= n:
                    result[i] = j - i
                    break
                result[i] = j - i + 1
        
        return result
