class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        result = 0
        for i in range(n):        
            if number[i] == digit:
                result = number[:i] + number[i+1:]
                if i + 1 < n and int(number[i]) < int(number[i+1]):
                    return result
        return result