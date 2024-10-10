class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        heroes = [(h, i) for i, h in enumerate(heroes)]
        monsters = [(m, c) for m, c in zip(monsters, coins)]
        heroes.sort()
        monsters.sort()
        result = [0 for _ in range(len(heroes))]
        coins = 0
        m = 0
        for h, i in heroes:
            while m < len(monsters) and h >= monsters[m][0]:
                coins += monsters[m][1]
                m += 1
            result[i] = coins
        return result
