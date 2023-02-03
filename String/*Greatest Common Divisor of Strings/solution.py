class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if there is a valid str, its length would be gcd(len(s1), len(s2))
        # prove: if gcd = x, divides = y, y < x
        # x % len(s1) == 0 && x % len(s2) == 0
        # y % len(s1) == 0 && y % len(s2) == 0
        # => x % y == 0
        # s1 = x * times = (y * z) * times => x must be also be divisible string 
        gcd = math.gcd(len(str1), len(str2))
        n, m = len(str1)//gcd, len(str2)//gcd
        s = str1[:gcd]
        return s if s * n == str1 and s * m == str2 else ""
