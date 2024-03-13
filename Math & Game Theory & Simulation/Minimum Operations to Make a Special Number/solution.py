class Solution:
    def minimumOperations(self, num: str) -> int:
        # 00 25 50 75
        n = len(num)
        result = n
        have_zero = False
        for last in ["00", "25", "50", "75"]:
            idx = len(last) - 1
            res = 0
            for i in range(n-1, -1, -1):
                if num[i] == "0":
                    have_zero = True
                if num[i] == last[idx]:
                    idx -= 1
                    if idx == -1:
                        result = min(result, res)
                        break
                else:
                    res += 1
        if have_zero:
            result = min(result, n-1)
        return result
