class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word[0] == "$" and word[1:].isdigit():
                cur = float(word[1:])
                cur = cur - cur * discount / 100
                words[i] = format(cur,".2f")
                words[i] = "$" + words[i]
        return " ".join(words)