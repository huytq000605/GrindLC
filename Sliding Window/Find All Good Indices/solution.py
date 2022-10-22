class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        before, after = deque(), deque()
        result = []
        for i in range(1, n-k):
            if before and nums[before[-1]] < nums[i-1]:
                before.clear()
            before.append(i-1)
            if before[0] == i - k - 1:
                before.popleft()
            
            if after and nums[after[-1]] > nums[i+k]:
                after.clear()
            after.append(i+k)
            if after[0] == i:
                after.popleft()

            if len(before) == k and len(after) == k:
                result.append(i)
        return result
