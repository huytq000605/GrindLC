class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        d = defaultdict(list)
        for word in words:
            d[word[0]].append(word)
        idx = 0
        while d and idx < len(s):
            nxt = defaultdict(list)
            for start_letter in d.keys():
                if start_letter == s[idx]:
                    for word in d[start_letter]]:
                        if len(word) == 1:
                            result += 1
                        else:
                            next_word = word[1:]
                            nxt[next_word[0]].append(next_word)
                else:
                    nxt[start_letter].append([*d[start_letter]])
            idx += 1
            d = nxt
        return result
