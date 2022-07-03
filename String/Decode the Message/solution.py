class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        count = 0
        idx = 0
        d = dict()
        c = ord('a')
        while count < 26:
            if key[idx] == " " or key[idx] in d:
                idx += 1
            else:
                d[key[idx]] = chr(c)
                c += 1
                count += 1
                idx += 1
        d[" "] = " "
        result = ""
        for l in message:
            result += d[l]
        return result
