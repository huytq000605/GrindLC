class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = [0 for _ in range(26)]
        for c in s:
            counter[ord(c) - ord('a')] += 1
        result = ""
        mid = ""
        for c, f in enumerate(counter):
            if not f: continue
            c = chr(c + ord('a'))
            if f&1:
                mid = c
            result += c * (f//2)
        return result + mid + result[::-1]
