class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev = -1
        wait_time = 0
        for a, t in customers:
            if a > prev:
                wait_time += t
                prev = a + t
            else:
                prev += t
                wait_time += prev - a
        return wait_time / (len(customers))

