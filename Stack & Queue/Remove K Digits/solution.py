class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr = []
        for digit in num:
            while k > 0 and len(arr) > 0 and arr[-1] > int(digit):
                k -= 1
                arr.pop()
            arr.append(int(digit))
        while k > 0:
            arr.pop()
            k -= 1

        result = ""
        leading_zero = True
        for digit in arr:
            if digit == 0 and leading_zero:
                continue
            leading_zero = False
            result += str(digit)
        if result == "":
            return "0"
        return result