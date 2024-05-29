class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        # Basically 4 and 7 are like 0, 1 in binary numbers
        # K - K Binary - Binary Output - Lucky Output
        # 1 - 01 - 10 - 4
        # 2 - 10 - 11 - 7
        # 3 - 11 - 100 - 44
        # 4 - 100 - 101 - 47
        # 5 - 101 - 110 - 74
        # => Output = K + 1 without MSB, replace 0 with 4, 1 with 7
        k += 1
        result = ""
        while k > 1:
            result += "7" if k & 1 else "4"
            k >>= 1
        return result[::-1] 
