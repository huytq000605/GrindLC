class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        dq = deque()
        result = 0
        for i in range(len(nums)):
            while dq and i - dq[0] >= k:
                dq.popleft()
            if (nums[i] + len(dq)) % 2 == 0:
                if i > len(nums) - k: return -1
                dq.append(i)
                result += 1
        return result
         
