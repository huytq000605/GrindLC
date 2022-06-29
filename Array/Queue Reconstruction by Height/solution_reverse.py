class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Place shorest people first
        people.sort()
        n = len(people)
        result = [[-1, -1] for i in range(n)]
        
        for h, k in people:
            # Idx to place this person
            idx = 0
            # Number of taller or equal people before this person
            not_shorter = 0
            # Find k taller or equal people
            while not_shorter < k:
                if result[idx][0] == -1 or result[idx][0] >= h:
                    not_shorter += 1
                idx += 1
            # Place to a valid place
            while result[idx][0] != -1:
                idx += 1
            result[idx] = [h, k]
        return result