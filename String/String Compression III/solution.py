class Solution:
    def compressedString(self, word: str) -> str:
        result = ""
        prev = word[0]
        count = 0
        for c in word:
            if c == prev:
                count += 1
                if count == 9:
                    result += "9" + c
                    count = 0
            else:
                if count:
                    result += str(count) + prev
                count = 1
            prev = c
        if count:
            result += str(count) + prev
        return result
