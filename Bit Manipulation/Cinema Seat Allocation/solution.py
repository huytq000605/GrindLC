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

"""
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        result = 2 * n
        reserved = defaultdict(lambda: [0 for _ in range(11)])
        for r, c in reservedSeats:
            if c == 1 or c == 10: continue
            reserved[r][c] = 1
        for rs in reserved.values():
            result -= 1
            if (rs[2] or rs[3] or rs[4] or rs[5]) and (rs[6] or rs[7] or rs[8] or rs[9]) and (rs[4] or rs[5] or rs[6] or rs[7]): 
                result -= 1
        return result
"""
