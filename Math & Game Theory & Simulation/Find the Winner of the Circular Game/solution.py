class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = [i for i in range(n)]
        i = 0
        while len(people) > 1:
            i = (i + (k-1)) % len(people)
            people.pop(i)
        return people[0] + 1
