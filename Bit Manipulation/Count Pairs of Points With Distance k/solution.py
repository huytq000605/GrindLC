class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        result = 0
        for x_xor in range(101):
            y_xor = k - x_xor
            d = defaultdict(dict)
            if y_xor < 0: continue
            for x_a, y_a in coordinates:
                x_b, y_b = x_xor ^  x_a, y_xor ^ y_a
                if x_b in d and y_b in d[x_b]:
                    result += d[x_b][y_b]

                d[x_a][y_a] = d[x_a].get(y_a, 0) + 1
        return result
