class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        s = sum(skill)
        if s % (n // 2) != 0:
            return -1
        each = s // (n//2)
        counter = Counter(skill)
        result = 0
        for v, freq in counter.items():
            if freq != counter[each - v]:
                return -1
            result += v * (each - v) * freq
        return result // 2
