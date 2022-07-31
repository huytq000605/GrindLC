class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # n*(n+1)/2 <= len(grades)
        start, end = 0, 1000
        val = len(grades) * 2
        while start < end:
            mid = start + math.ceil((end-start)/2)
            if mid * (mid+1) <= val:
                start = mid
            else:
                end = mid - 1
        return start
