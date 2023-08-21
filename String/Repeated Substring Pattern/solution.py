class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # assume s = n * s1 = s1s1s1...s1
        # s + s = n * 2 * s1 = s1s1s1....s1
        # delete first and last char
        # modified(s + s) = xs1s1s1....s1y
        # (n*2 - 2) * s1 witn n >= 2 => (n*2 - 2) >= n
        # (n*2 - 2) * s1 >= n * s1 >= s
        # contains s1
        
        # return s in (s + s)[1:-1]
        
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i != 0: continue
            times = n // i
            if s[:i] * times == s:
                return True
        return False
