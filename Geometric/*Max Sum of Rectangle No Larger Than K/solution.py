from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # Maximum subarray with sum <= k
        def max_sub_array(arr, k):
            total = 0
            ans = -math.inf
            seen_total = SortedList([0])
            for num in arr:
                total += num
                idx = seen_total.bisect_left(total - k)
                if idx < len(seen_total):
                    ans = max(ans, total - seen_total[idx])
                seen_total.add(total)
            return ans
        result = -math.inf
        m, n = len(matrix), len(matrix[0])
        # We calculate for every pairs of r1, r2 (Every rectangle have rows from r1 to r2)
        # arr[i] = sum(matrix[r][i] for r1 <= r <= r2)
        # We can reuse arr through r2
        for r1 in range(m):
            arr = [0 for i in range(n)]
            for r2 in range(r1, m):
                for c in range(n):
                    arr[c] += matrix[r2][c]
                result = max(result, max_sub_array(arr, k))
        return result
                    