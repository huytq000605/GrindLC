class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 3 * pow(2, n-1) < k: return ""
        result = ""
        options = pow(2, n-1)
        for i in range(n):
            for c in range(3):
                if result and result[-1] == chr(c + ord('a')): continue
                if k - options <= 0:
                    result += chr(c + ord('a'))
                    break
                k -= options
            options //= 2
        return result
