class Solution:
    def minimumMoves(self, nums: List[int], k: int, changes: int) -> int:
        ones = [i for i, num in enumerate(nums) if num == 1]
        if not ones:
            return k * 2
        
        prefix = [0 for _ in range(len(ones))]
        for i in range(len(ones)):
            if i > 0: prefix[i] = prefix[i-1]
            prefix[i] += ones[i]
        def get_sum(left, right):
            if left == 0: return prefix[right]
            return prefix[right] - prefix[left-1] 

        result = math.inf
        min_step2 = max(0, k - changes - 1) # -1 for the alice index
        # min_steps2 + 3 due to the 2 adjacent ones can be better than using step1
        for step2 in range(min_step2, min_step2 + 3):
            if step2 + 1 > k: break
            step1 = k - 1 - step2
            for left in range(len(ones)):
                # right - left + 1 == steps2 + 1
                right = left + step2
                if right >= len(ones): break
                median = left + (right - left) // 2
                left_step2 = -get_sum(left, median) + ones[median] * (median - left + 1)
                right_step2 = get_sum(median, right) - ones[median] * (right - median + 1)
                result = min(result, step1 * 2 + left_step2 + right_step2)
        return result
