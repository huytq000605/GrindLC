class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(int)
        left = sum([1 << i for i in range(2, 6)])
        mid = sum([1 << i for i in range(4, 8)])
        right = sum([1 << i for i in range(6, 10)])
        for row, seat in reservedSeats:
            reserved[row] |= (1 << seat)
        result = 2 * n
        for row in reserved.keys():
            count = 0
            if left & reserved[row] == 0:
                count += 1
            if right & reserved[row] == 0:
                count += 1
            if count == 0 and mid & reserved[row] == 0:
                count = 1
            result -= (2-count)
        return result
