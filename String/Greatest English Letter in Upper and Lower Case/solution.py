class Solution:
    def greatestLetter(self, s: str) -> str:
        counter = Counter(s)
        result = ""
        for l in string.ascii_uppercase:
            if counter[l] > 0 and counter[l.lower()] > 0:
                result = l
        return result