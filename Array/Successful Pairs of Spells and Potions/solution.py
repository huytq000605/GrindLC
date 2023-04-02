class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        spells = sorted([(spells[i], i) for i in range(n)])
        potions.sort(reverse = True)
        p = 0
        result = [0 for _ in range(n)]
        for spell, idx in spells:
            while p < m and potions[p] * spell >= success:
                p += 1
            result[idx] = p
        return result
