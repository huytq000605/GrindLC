class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        count = Counter()
        for r, c in coordinates:
            # top left
            if r + 1 < m and c + 1 < n: count[(r, c)] += 1
            # top right
            if r + 1 < m and c - 1 >= 0: count[(r, c-1)] += 1
            # btm left
            if r - 1 >= 0 and c + 1 < n: count[(r-1, c)] += 1
            # btm right
            if r - 1 >= 0 and c - 1 >= 0: count[(r-1, c-1)] += 1

        result = [(m-1)*(n-1), 0, 0, 0, 0]
        for black_count in count.values():
            result[black_count] += 1
            result[0] -= 1
        return result
