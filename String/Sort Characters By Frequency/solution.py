class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for l in s:
            freq[l] = freq.get(l, 0) + 1
        result = ""
        sortedFreq = sorted(list(freq.items()), key = lambda f: -f[1])
        for k, f in sortedFreq:
            result += k * f
        return result