class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(reverse = True)
        n = len(spells)
        spells_with_idx = sorted([(spells[i], i) for i in range(n)])
        result = [0 for i in range(n)]
        idx = 0
        for spell, i in spells_with_idx:
            while idx < len(potions) and potions[idx] * spell >= success:
                idx += 1
            result[i] = idx
        return result