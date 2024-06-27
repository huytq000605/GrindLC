class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        remember = 0
        # if bit == 1
            # if carry = 1, res += 1
            # if carry = 0, res += 2
        # if bit == 0
            # if carry = 1, res += 2
            # if carry = 0, res += 1
        for i in range(len(s) - 1, 0, -1):
            if ord(s[i]) - ord('0') + remember == 1:
                remember = 1
                result += 1
            result += 1
        return result + remember
