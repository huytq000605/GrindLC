class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = [0 for _ in range(n)]
        i = 0
        times = 1
        while True:
            if seen[i]:
                break
            seen[i] = 1
            i += k * times
            times += 1
            k %= n
            i %= n
        result = []
        for i, s in enumerate(seen):
            if not s: result.append(i + 1)
        return sorted(result)
