class Codec:
    def _encode(self, s):
        if not s: return ""
        result = ""
        for c in s:
            result += str(ord(c))
            result += ","
        return result[:-1]
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            result += self._encode(s)
            result += "."
        return result[:-1]
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return list(map(self._decode, s.split(".")))
    
    def _decode(self, s):
        result = ""
        for s in s.split(","):
            if not s: 
                continue
            result += chr(int(s))
        return result
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
