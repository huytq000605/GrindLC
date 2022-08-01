class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        result = 1
        for roll in rolls:
            seen.add(roll)
            if len(seen) == k:
                result += 1
                seen.clear()
        return result
