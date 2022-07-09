class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            while i - dq[0][1] > k:
                dq.popleft()
            new_place = dq[0][0] + nums[i]
            while dq and dq[-1][0] <= new_place:
                dq.pop()
            dq.append((new_place, i))
        return dq[-1][0]
