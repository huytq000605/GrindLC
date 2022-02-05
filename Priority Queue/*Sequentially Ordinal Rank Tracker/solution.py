from heapq import heappush, heappop

class Node():
    def __init__(self, score, name):
        self.score = score
        self.name = name
    
    def __lt__(self, other):
        if self.score == other.score:
            return self.name > other.name
        return self.score < other.score

class SORTracker:

    def __init__(self):
        self.top = []
        self.bot = []
        self.n = 0

    def add(self, name: str, score: int) -> None:
        heappush(self.top, Node(score, name))
        while len(self.top) > self.n:
            minTop = heappop(self.top)
            heappush(self.bot, [-minTop.score, minTop.name])

    def get(self) -> str:
        self.n += 1
        result = self.bot[0][1]
        score, name = heappop(self.bot)
        score = -score
        heappush(self.top, Node(score, name))
        return result


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()