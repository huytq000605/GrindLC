class Solution:
    def stringIndices(self, containers: List[str], queries: List[str]) -> List[int]:
        trie = dict()
        KEY = 'word'
        for i, word in enumerate(containers):
            cur = trie
            if KEY not in cur or len(word) < len(containers[cur[KEY]]):
                cur[KEY] = i
                
            for c in word[::-1]:
                if c not in cur: cur[c] = dict()
                cur = cur[c]
                
                if KEY not in cur or len(word) < len(containers[cur[KEY]]):
                    cur[KEY] = i

        result = []
        for query in queries:
            cur = trie
            res = -1
            for c in query[::-1]:
                if c not in cur: break
                cur = cur[c]
            res = cur[KEY]
            result.append(res)
        return result
            
