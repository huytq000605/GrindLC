class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        times = [k//26 for i in range(26)]
        n = len(s)
        for diff in range(k % 26 + 1):
            times[diff] += 1

        for i in range(n):
            if s[i] != t[i]:
                from_letter = ord(s[i]) - ord('a')
                to_letter = ord(t[i]) - ord('a')
                if to_letter < from_letter:
                    to_letter += 26
                diff = to_letter - from_letter
                if times[diff] > 0 and k > 0:
                    times[diff] -= 1
                    k -= 1
                else:
                    return False
        return True
