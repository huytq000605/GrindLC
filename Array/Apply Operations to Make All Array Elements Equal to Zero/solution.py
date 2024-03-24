class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dq = deque()
        s = 0
        for i, num in enumerate(nums):
            while dq and i - dq[0][0] >= k:
                s -= dq.popleft()[1]
            if num - s < 0: return False
            if num - s:
                if i + k - 1 >= n: return False
                dq.append((i, num-s))
                s = num
        return True 
        
