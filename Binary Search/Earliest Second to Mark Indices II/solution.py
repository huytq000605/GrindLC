class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)

        # i = second (0-indexed)
        # j = index in nums

        # first[j] = the first second we met nums[j]
        # note that we only care if nums[j] = 0, otherwise we dont need zero operation
        first = dict()
        for i, j in enumerate(changeIndices):
            if nums[j-1] > 0 and j-1 not in first:
                first[j-1] = i

        def possible(last_m):
            marks = 0
            # pq stores all the nums[j] we use zero operation -> mark operation
            pq = []
            for i in range(last_m, -1, -1):
                j = changeIndices[i] - 1
                # if we zero some index, we always zero it at the first time we met it
                if j in first and first[j] == i:
                    heappush(pq, nums[j])
                    # Because we use the operation to make nums[j] = 0
                    # There must be mark operation happen after that
                    # But there might be case we don't have any mark operation
                    # Or that mark operation has been used for another num
                    # We used pq to determine the smaller num must be handle by decrement by 1 until 0
                    if marks:
                        marks -= 1
                    else:
                        heappop(pq)
                        marks += 1
                else:
                    marks += 1
            
            # len(nums) - len(pq) = remaining num need to be marked
            # sum(nums) - sum(pq) = sum of remaining num need to be marked
            return len(nums) - len(pq) + sum(nums) - sum(pq) <= marks

        start, end = 0, m
        while start < end:
            mid = start + (end - start) // 2
            if possible(mid):
                end = mid
            else:
                start = mid + 1
        if start == m:
            return -1
        return start + 1
            
