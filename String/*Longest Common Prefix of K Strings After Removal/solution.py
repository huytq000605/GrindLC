class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.count = 0
        self.best_prefix_length = 0
        

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        trie = TrieNode()
        for word in words:
            self.update_trie(trie, word, 1, k)
        
        result = []
        for word in words:
            self.update_trie(trie, word, -1, k)
            result.append(trie.best_prefix_length)
            self.update_trie(trie, word, 1, k)
        return result 

    def update_trie(self, trie, word, delta, k):
        t = trie
        path = [t]
        for c in word:
            i = ord(c) - ord('a')
            if not t.children[i]: 
                t.children[i] = TrieNode()
            t.children[i].count += delta
            t = t.children[i]
            path.append(t)

        for i in range(len(path)-1, -1, -1):
            t = path[i]
            t.best_prefix_length = 0
            if t.count >= k:
                t.best_prefix_length = i
            
            for child in t.children:
                if child:
                    t.best_prefix_length = max(t.best_prefix_length, child.best_prefix_length)
                
        
        
        
