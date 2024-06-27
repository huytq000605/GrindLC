class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        counter = Counter(words[0])
        for word in words[1:]:
            new_counter = Counter()
            c = Counter(word)
            for k, v in c.items():
                new_counter[k] = min(v, counter[k])
            counter = new_counter
        result = []
        for k, v in counter.items():
            for _ in range(v): result.append(k)
        return result
