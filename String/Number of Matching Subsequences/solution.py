class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        d = defaultdict(list)
        for word in words:
            d[word[0]].append((word, 0))

        # len(words[i]) <= 50
        # Time complexity: len(s) + len(S) with S is total length of every word in words 
        for c in s:
            for starting in d.keys():
                if starting == c:
                    continue
                nxt[starting] = d[starting]

            if c in d:
                for word, idx in d[c]:
                    idx += 1
                    if idx == len(word):
                        result += 1
                    else:
                        nxt[word[idx]].append((word, idx))
            d = nxt
        return result
