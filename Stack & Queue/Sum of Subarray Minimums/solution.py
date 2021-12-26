class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr = [-math.inf, *arr, -math.inf]
        MOD = 10**9 + 7
        result = 0
        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                current = stack.pop()
                nextSmaller = i
                prevSmaller = stack[-1]
                result += arr[current] * (current - prevSmaller) * (nextSmaller - current)
                result %= MOD
            stack.append(i)
        return result