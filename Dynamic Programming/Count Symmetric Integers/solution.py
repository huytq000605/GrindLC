class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 1: continue
            else:
                n = len(s)
                first, last = 0, 0
                for i in range(n):
                    if i < n // 2: first += int(s[i])
                    else: last += int(s[i])
                if first == last:
                    result += 1
        return result
