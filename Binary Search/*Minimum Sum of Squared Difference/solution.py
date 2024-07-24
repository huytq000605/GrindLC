class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [0 for i in range(n)]
        for i in range(n):
            diff[i] = abs(nums1[i] - nums2[i])
        low = 0
        hi = max(diff)
        max_move = k1 + k2
        if max_move >= sum(diff):
            return 0

        # Binary search to find the target which we can decrease all numbers > target to
        while low < hi:
            mid = low + (hi - low) // 2
            moves = 0
            for num in diff:
                if num <= mid:
                    continue
                else:
                    moves += num - mid
            if moves > max_move:
                low = mid + 1
            else:
                hi = mid
        target = low

        # Try to find if we still have some moves
        # max_move now is equal to remaining moves
        for num in diff:
            if num <= target:
                continue
            else:
                max_move -= num - target

        result = 0
        for num in diff:
            if num < target:
                result += num ** 2
            else:
                # If we still have moves, we -1 for each remaining moves
                if max_move > 0:
                    result += (target - 1) ** 2
                    max_move -= 1
                else:
                    result += target ** 2
        return result
