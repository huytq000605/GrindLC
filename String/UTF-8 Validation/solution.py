class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        while idx < len(data):
            first = data[idx]
            if (first >> 7) & 1 == 0:
                idx += 1
                continue
            n = -1
            for i in range(7, 2, -1):
                if (first >> i) & 1 == 0:
                    n = 7-i
                    break
            if n <= 1 or idx + n - 1  >= len(data):
                return False

            for i in range(idx + 1, idx + n):
                if (data[i] >> 6) != 0b10:
                    return False
            idx = idx + n
        return True
