class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0 for i in range(n)]
        for i in range(n):
            score[edges[i]] += i
        max_score, idx = -1, -1
        for i, s in enumerate(score):
            if s > max_score:
                idx = i
                max_score = s
        return idx
