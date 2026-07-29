class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = dict()
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = dict()
                t = t[c]
            t['word'] = word
        result = ""
        dq = deque([])
        for c in trie:
            if 'word' in trie[c]:
                dq.append(trie[c])
        while dq:
            t = dq.popleft()
            if len(t['word']) > len(result) or (len(t['word']) == len(result) and t['word'] < result):
                result = t['word'] 
            for c in t:
                if c == 'word': continue
                if 'word' not in t[c]: continue
                dq.append(t[c])
        return result
