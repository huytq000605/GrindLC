class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = -1
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                result = max(result, int(num[i]))
        if result == -1:
            return ""
        return str(result) * 3