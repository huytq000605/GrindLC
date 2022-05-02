class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefix = set()
        current = ""
        for l in s:
            current += l
            prefix.add(current)
        
        result = 0
        for word in words:
            if word in prefix:
                result += 1
        return result