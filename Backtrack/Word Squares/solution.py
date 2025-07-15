class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        result = []
        cur = []
        trie = dict()
        for word in words:
            a = trie
            for c in word:
                if c not in a:
                    a[c] = dict()
                a = a[c]
                if 'words' not in a: a['words'] = []
                a['words'].append(word)
        m = len(words[0])
        def dfs(i):
            if i == m:
                result.append([*cur])
                return
            elif i == 0:
                for word in words:
                    cur.append(word)
                    dfs(i+1)
                    cur.pop()
            else:
                a = trie
                for j in range(i):
                    if cur[j][i] not in a:
                        a = None
                        break
                    a = a[cur[j][i]]
                if a is None:
                    return
                for word in a['words']:
                    cur.append(word)
                    dfs(i+1)
                    cur.pop()
        dfs(0)
        return result
