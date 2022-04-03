import collections

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.key_to_idx = dict()
        for i, key in enumerate(keys):
            self.key_to_idx[key] = i
        self.keys = keys
        self.values = values
        self.value_to_idx = collections.defaultdict(list)
        for i, value in enumerate(values):
            self.value_to_idx[value].append(i)
        self.trie = {}
        for word in dictionary:
            current = self.trie
            for l in word:
                if l not in current:
                    current[l] = {}
                current = current[l]
            current['word'] = True

    def encrypt(self, word1: str) -> str:
        result = ""
        for l in word1:
            result += self.values[self.key_to_idx[l]]
        return result

    def decrypt(self, word2: str) -> int:
        result = [("", self.trie)]
        for i in range(0, len(word2), 2):
            value = word2[i:i+2]
            idxs = self.value_to_idx[value]
            new_result = []
            for idx in idxs:
                c = self.keys[idx]
                for s, current in result:
                    if c in current:
                        new_result.append((s + c, current[c]))
            result = new_result
        num = 0
        for s, current in result:
            if 'word' in current:
                num += 1
        return num
        
                


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)