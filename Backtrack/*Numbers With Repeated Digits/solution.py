@cache
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

@cache
def permutation(k, n):
    return int(factorial(n) / factorial(n-k))

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        out_bound = list(map(int, str(n + 1))) # n + 1
        max_length = len(out_bound)
        no_repeated_digits = 0
        # Calculate all number have length < len(out_bound)
        for i in range(1, len(out_bound)):
            no_repeated_digits += 9 * permutation(i - 1, 9)

        used = set()
        # Calculate all number have length == len(out_bound)
        for i in range(max_length):
            digit = out_bound[i]
            start = 0
            if i == 0:
                start = 1
            # Try to fill i position with j
            for j in range(start, digit):
                if j in used:
                    continue
                # Fill i position with j (j < digit)
                no_repeated_digits += permutation(max_length - 1 - i, 9 - i)
            # Fill i position with digit (if digit has been used => cannot)
            if digit in used:
                break
            used.add(digit)

        return int(n) - no_repeated_digits