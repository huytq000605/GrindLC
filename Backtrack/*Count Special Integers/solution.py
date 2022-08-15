class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        def P(k, n):
            return int(math.factorial(n) / math.factorial(n-k))
        n = list(map(int, str(n)))
        m = len(n)
        result = 0
        used = set()
        def count_equal_length(idx):
            nonlocal result, used, m
            if idx >= m:
                # Count num == n
                result += 1
                return
            start = 0
            if idx == 0:
                start = 1
            remaining_digits = 10 - len(used) - 1
            positions = m - (idx + 1)
            for i in range(start, n[idx]):
                if i in used:
                    continue
                result += P(positions, remaining_digits)
            if n[idx] not in used:
                used.add(int(n[idx]))
                count_equal_length(idx + 1)
        
        # 1 digits to m digits
        for i in range(1, m):
            # First digit cannot be zero, so we * 9
            result += P(i - 1, 9) * 9
        count_equal_length(0)
        return result
