class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda course: course[1])
        pq = []
        time = 1
        for duration, last_day in courses:
            # valid state, try to learn 1 course
            heappush(pq, -duration)
            time += duration
            # if cannot learn this course, pop biggest course we've learnt
            if time - 1 > last_day:
                time -= -heappop(pq)
        return len(pq)
