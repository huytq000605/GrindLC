class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        dq = deque()
        for num in nums:
            while dq and num - dq[0] > 2*k:
                dq.popleft()
            dq.append(num)
            result = max(result, len(dq))
        return result
