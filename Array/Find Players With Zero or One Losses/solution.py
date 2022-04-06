class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_all = set()
        lose = Counter()
        for winner, loser in matches:
            if winner not in lose:
                win_all.add(winner)
            win_all.discard(loser)
            lose[loser] += 1
        
        lose_one = []
        for loser, num in lose.items():
            if num == 1:
                lose_one.append(loser)
        return [sorted(win_all), sorted(lose_one)]