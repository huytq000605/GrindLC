class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # Get max_sum by sum all positive integers
        max_sum = sum([max(num, 0) for num in nums])
        # We start from max_sum, generate all subsequences
        # If meet negative integer, can ignore it
        # If meet positive integer, can exclude it
        # For each num generate 2 branches
        # One for exclude/ignore the number at idx i
        # Another for adding back the number at idx i - 1 and exclude/ignore number at idx i
        abs_nums = sorted([abs(num) for num in nums])
        pq = [(-max_sum, 0)]
        n = len(nums)
        for i in range(k-1):
            s, i = heappop(pq)
            if i < n:
                heappush(pq, (s + abs_nums[i], i + 1))
                if i > 0:
                    heappush(pq, (s - abs_nums[i-1] + abs_nums[i], i + 1))
        return -pq[0][0]