class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = dict()
        for word in dictionary:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = dict()
                cur = cur[c]
            cur["is_word"] = True
        result = ""
        for word in sentence.split(" "):
            if result: result += " "
            cur = trie
            for c in word:
                if cur: cur = cur.get(c, None)
                result += c
                if cur and "is_word" in cur:
                    break
        return result
