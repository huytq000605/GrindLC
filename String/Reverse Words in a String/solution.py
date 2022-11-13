class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for c in s:
            if c == " ":
                if word:
                    words.append(word)
                    word = ""
            else:
                word += c
        if word:
            words.append(word)
        return " ".join(words[::-1])
            
