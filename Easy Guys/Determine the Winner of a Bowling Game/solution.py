class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1, p2 = 0, 0
        n = len(player1)
        for i in range(n):
            p1 += player1[i]
            p2 += player2[i]
            if i >= 1:
                if player1[i-1] == 10 or player1[max(0, i-2)] == 10:
                    p1 += player1[i]
                if player2[i-1] == 10 or player2[max(0, i-2)] == 10:
                    p2 += player2[i]
        if p1 > p2:
            return 1
        elif p1 < p2:
            return 2
        else:
            return 0
