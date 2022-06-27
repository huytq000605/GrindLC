class Solution:
    def minPartitions(self, n: str) -> int:
        # Think on each digit
        # 82734
        # =
        # 11011 +
        # 11111 +
        # 10111 +
        # 10101 +
        # 10100 +
        # ...
        result = 0
        for l in n:
            result = max(result, int(l))
        return result
