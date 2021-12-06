class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            freq = dict()
            for l in word:
                freq[l] = freq.get(l, 0) + 1
            for charCode in range(ord("a"), ord("z") + 1):
                l = chr(charCode)
                if l in freq:
                    return freq[l]
        
        points = []
        for word in words:
            points.append(f(word))
            
        result = []
        for query in queries:
            cmpPoint = f(query)
            res = 0
            for point in points:
                if cmpPoint < point:
                    res += 1
            result.append(res)
        return result