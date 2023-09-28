class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        before = deque()
        j = 1
        used = 0
        reused = 0
        skipped = set()
        for i in range(n):
            if i in skipped:
                continue
            while j < n and nums[i] >= nums[j]:
                j += 1
            if j < n and nums[j] > nums[i]:
                before.append(i)
                before.append(j)
                skipped.add(j)
                used += 2
                j += 1
            elif before and nums[before[0]] < nums[i]:
                before.popleft()
                reused += 1
        return n - used - reused // 2 * 2
        
                
                
