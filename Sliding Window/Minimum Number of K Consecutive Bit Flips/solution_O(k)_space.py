class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flip = 0
        flipped = deque()
        result = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if len(flipped) > 0 and i - flipped[0] == k:
                flipped.popleft()
                flip -= 1
            if i <= n - k:
                if (num == 0 and flip % 2 == 0) or (num == 1 and flip % 2 == 1):
                    flipped.append(i)
                    flip += 1
                    result += 1
            else:
                if (num == 0 and flip % 2 == 0) or (num == 1 and flip % 2 == 1):
                    return -1
        return result