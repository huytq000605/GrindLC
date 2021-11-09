class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        current = ""
        arr = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                arr.append(int(current))
                arr.append(expression[i])
                current = ""
            else:
                current += expression[i]
        arr.append(int(current))

        dp = [[None for j in range(len(arr))] for i in range(len(arr))]

        def generate(start, end):
            if dp[start][end] != None: return dp[start][end]
            result = []
            if start == end:
                result.append(arr[start])
                return result
            for i in range(start + 1, end, 2):
                if arr[i] == "+":
                    for n1 in generate(start, i - 1):
                        for n2 in generate(i + 1, end):
                            result.append(n1 + n2)
                if arr[i] == "-":
                    for n1 in generate(start, i - 1):
                        for n2 in generate(i + 1, end):
                            result.append(n1 - n2)
                if arr[i] == "*":
                    for n1 in generate(start, i - 1):
                        for n2 in generate(i + 1, end):
                            result.append(n1 * n2)
            dp[start][end] = result
            return result
        return generate(0, len(arr) - 1)
            