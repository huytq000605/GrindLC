class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        n = len(report)
        pq = []
        for i in range(n):
            id = student_id[i]
            r = report[i].split(" ")
            p = 0
            for word in r:
                if word in pos:
                    p += 3
                if word in neg:
                    p -= 1
            heappush(pq, (p, -id))
            if len(pq) > k:
                heappop(pq)
        return map(lambda e: -e[1], sorted(pq)[::-1])
                    
            
