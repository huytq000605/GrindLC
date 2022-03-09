class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        seen = set()
        result = math.inf
        for num in arr:
            new_seen = set()
            for value in seen:
                result = min(result, abs((value & num) - target))
                new_seen.add(value & num)
            new_seen.add(num)
            seen = new_seen
            result = min(result, abs(num-target))
        return result