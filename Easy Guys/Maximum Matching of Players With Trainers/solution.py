class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i, j = 0, 0
        result = 0
        while i < m and j < n:
            if players[i] <= trainers[j]:
                i += 1
                j += 1
                result += 1
            else:
                j += 1
        return result
