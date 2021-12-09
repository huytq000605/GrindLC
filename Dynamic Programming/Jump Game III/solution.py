class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        seen.add(start)
        stack = [start]
        while stack:
            currentPos = stack.pop()
            if arr[currentPos] == 0:
                return True
            for nextPos in [currentPos + arr[currentPos], currentPos - arr[currentPos]]:
                if nextPos in seen or nextPos < 0 or nextPos >= len(arr):
                    continue
                seen.add(nextPos)
                stack.append(nextPos)
        return False