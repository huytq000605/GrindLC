class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        high_employees = set()
        accesses = []
        for e, t in access_times:
            m = int(t[:2]) * 60 + int(t[2:])
            accesses.append((m, e))
        accesses.sort()
        seen = defaultdict(deque)
        for t, e in accesses:
            while e in seen and (len(seen[e]) >= 3 or (seen[e] and t > seen[e][0] + 59)):
                seen[e].popleft()
            seen[e].append(t)
            if len(seen[e]) == 3:
                high_employees.add(e)
        return list(high_employees)
