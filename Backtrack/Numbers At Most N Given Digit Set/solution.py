class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        length_of_n = len(n)
        result = 0
        for no_of_digits in range(1, length_of_n):
            result += len(digits) ** no_of_digits
        def dfs(digit):
            if digit >= len(n):
                return 1
            result = 0
						# Can increase performance with binary search
            for d in digits:
                if int(d) > int(n[digit]):
                    break
                elif int(d) == int(n[digit]):
                    result += dfs(digit + 1)
                else:
                    result += len(digits) ** (len(n) - (digit + 1))
            return result
        
        result += dfs(0)
        return result
                    