class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = defaultdict(list)
        for i, s in items:
            heappush(students[i], s)
            if len(students[i]) > 5:
                heappop(students[i])
        result = [[i, sum(s) // 5] for i, s in sorted(students.items())]
        return result
