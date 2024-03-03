class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        if sum(nums) + n > m:
            return -1
        
        def possible(last_m):
            removes = 0
            marked = set()
            for i in range(last_m, -1, -1):
                j = changeIndices[i] - 1
                if j in marked:
                    if removes:
                        removes -= 1
                else:
                    removes += nums[j]
                    marked.add(j)
            return removes == 0 and len(marked) == n

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
            
