class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences = sorted([1, *hFences, m])
        vFences = sorted([1, *vFences, n])
        vertical_sides = set()
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                vertical_sides.add(vFences[j] - vFences[i])
        result = -1
        MOD = 10**9 + 7
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                side = hFences[j] - hFences[i]
                if side in vertical_sides:
                    result = max(result, side)
        if result == -1:
            return -1
        return (result * result) % MOD
