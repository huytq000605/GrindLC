class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        wins = 0
        cur = skills[0]
        cur_idx = 0
        for i, s in enumerate(skills):
            if i == 0: continue
            if s > cur:
                cur = s
                cur_idx = i
                wins = 0
            wins += 1
            if wins == k:
                return cur_idx
        return cur_idx
