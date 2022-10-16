class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longest_work, longest_worker = -1, 0
        prev = 0
        for id, leave in logs:
            if (leave - prev) > longest_work or ((leave - prev) == longest_work and id < longest_worker):
                longest_work = leave - prev
                longest_worker = id
            prev = leave
        return longest_worker
