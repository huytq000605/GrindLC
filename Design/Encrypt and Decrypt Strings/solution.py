class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.mapping = dict()
        for i in range(len(keys)):
            self.mapping[keys[i]] = values[i]
        self.counter = Counter()
        
        for word in dictionary:
            encrypted = self.encrypt(word)
            self.counter[encrypted] += 1

    def encrypt(self, word1: str) -> str:
        result = ""
        for l in word1:
            result += self.mapping[l]
        return result

    def decrypt(self, word2: str) -> int:
        return self.counter[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)