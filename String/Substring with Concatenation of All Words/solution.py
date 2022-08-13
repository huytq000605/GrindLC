class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = Counter(words)
        word_length = len(words[0])
        length_need = word_length * len(words)
        def is_concatenation(idx):
            nonlocal count, word_length, length_need
            seen = Counter()
            for i in range(idx, idx + length_need, word_length):
                word = s[i:i+ word_length]
                if word not in count:
                    return False
                seen[word] += 1
            for word, freq in count.items():
                if word not in seen or freq != seen[word]:
                    return False
            return True
        result = []
        for i in range(0, len(s) - length_need + 1):
            if is_concatenation(i):
                result.append(i)
        return result
