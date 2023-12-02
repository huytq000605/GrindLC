class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        result = 0
        for word in words:
            c = Counter(word)
            valid = True
            for ch in c.keys():
                if ch not in counter or c[ch] > counter[ch]:
                    valid = False
                    break
            if valid: result += len(word)
        return result
