class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        nums = nums[::-1]
        result = 0
        dq = deque()
        j = 0
        for i, num in enumerate(nums):
            while dq and num > nums[dq[-1]]:
                r = dq.pop()
                l = j-1 if not dq else dq[-1]
                k -= (r-l) * (num - nums[r])
            dq.append(i)
            while k < 0:
                # shrinking window, return back the value.
                # each value at j needs to be at least nums[dq[0]]
                k += nums[dq[0]] - nums[j]
                if dq and j == dq[0]: dq.popleft()
                j += 1
            result += i - j + 1
        return result
