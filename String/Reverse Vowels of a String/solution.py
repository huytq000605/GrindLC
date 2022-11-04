class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in "aeoiuAEOIU":
                i += 1
            while j > i and s[j] not in "aeoiuAEOIU":
                j -= 1
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        return "".join(a)
