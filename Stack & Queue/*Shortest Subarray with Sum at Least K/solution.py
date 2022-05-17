class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dequeue = deque()
        result = n+1
        current = 0
        for i, num in enumerate(nums):
            current += num
            if current >= k:
                result = min(result, i + 1)
            while dequeue and current - dequeue[0][1] >= k:
                result = min(result, i - dequeue.popleft()[0])
            while dequeue and current <= dequeue[-1][1]:
                dequeue.pop()
            dequeue.append([i, current])
        if result == n+1:
            return -1
        return result