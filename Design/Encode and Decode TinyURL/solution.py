class Codec:
    def __init__(self):
        self.decoded = dict()
        self.encoded = dict()
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.encoded:
            code = "".join(map(str, random.choices(self.chars, k = 6)))
            if code not in self.decoded:
                self.encoded[longUrl] = code
                self.decoded[code] = longUrl
        return self.encoded[longUrl]
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decoded[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))