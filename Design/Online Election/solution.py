class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = len(persons)
        self.maximum = [[0, 0] for i in range(n)]
        votes = collections.defaultdict(int)
        cur_max = 0
        for i in range(n):
            time = times[i]
            person = persons[i]
            self.maximum[i][0] = time
            votes[person] += 1
            if votes[person] >= cur_max:
                cur_max = votes[person]
                self.maximum[i][1] = person
            else:
                self.maximum[i][1] = self.maximum[i-1][1]
            

    def q(self, t: int) -> int:
        start = 0
        end = len(self.maximum) - 1
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if self.maximum[mid][0] == t:
                return self.maximum[mid][1]
            if self.maximum[mid][0] > t:
                end = mid - 1
            else:
                start = mid
        return self.maximum[start][1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)