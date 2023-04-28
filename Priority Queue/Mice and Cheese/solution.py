class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        s = sum(reward2)
        pq = []
        n = len(reward1)
        for i in range(n):
            heappush(pq, reward1[i] - reward2[i])
            if len(pq) > k:
                heappop(pq)
        return s + sum(pq)
