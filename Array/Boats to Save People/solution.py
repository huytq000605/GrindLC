class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        result = 0
        while i <= j:
            if i != j and people[j] + people[i] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            result += 1
        return result
