class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split("+")
        n, m = len(left), len(right)
        min_value = math.inf
        result = ""
        for i in range(n):
            for j in range(1, m + 1):
                if left[:i] == "":
                    left_mul = 1
                else:
                    left_mul = int(left[:i])
                if right[j:] == "":
                    right_mul = 1
                else:
                    right_mul = int(right[j:])
                after = f"{left[:i]}({left[i:]}+{right[:j]}){right[j:]}"
                
                value = left_mul * (int(left[i:]) + int(right[:j])) * right_mul
                if value < min_value:
                    result = after
                    min_value = value
        return result