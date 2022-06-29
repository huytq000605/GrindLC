class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # We are sorting the people by -height and break even with k
        # Because after sorted by -height, when we go to people[i]
        # We are sure that there is no more people are taller than this guy, than k is his index
        # People don't care about who shorter than them
        people.sort(key = lambda person: (-person[0], person[1]))
        result = []
        for h, k in people:
            result.insert(k, (h, k))
        return result