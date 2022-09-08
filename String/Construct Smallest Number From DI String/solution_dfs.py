class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        digits = [i+1 for i in range(n+1)]
        def permutations(i):
            if i >= len(digits):
                for j in range(n):
                    if pattern[j] == "D" and digits[j] < digits[j+1]:
                            return False
                    elif pattern[j] == "I" and digits[j] > digits[j+1]:
                            return False
                return True
            for j in range(i, len(digits)):
                digits[i], digits[j] = digits[j], digits[i]
                if permutations(i+1):
                    return True
                digits[i], digits[j] = digits[j], digits[i]
        permutations(0)
        return "".join(map(str, digits))
                
                    
