class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        while num > 0:
            binary += str(num % 2)
            num //= 2
        result = 0
        for i in range(len(binary)):
            if binary[i] == "0":
                result += 1 << i
        return result