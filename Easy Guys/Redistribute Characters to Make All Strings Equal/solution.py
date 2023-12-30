class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        counter = Counter()
        for word in words:
            for c in word:
                counter[c] += 1
        for k, v in counter.items():
            if v % n != 0:
                return False
        return True
        
