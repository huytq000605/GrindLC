class Solution:
    def robotWithString(self, s: str) -> str:
        t = []
        counter = Counter()
        for c in s:
            counter[ord(c)] += 1
        i = 0
        n = len(s)
        result = ""
        while i < n or t:
            if t:
                valid = True
                for j in range(t[-1]-1, ord('a') - 1, -1):
                    if counter[j] > 0:
                        valid = False
                        break
                if valid:
                    result += chr(t.pop())
                    continue
            
            t.append(ord(s[i]))
            counter[ord(s[i])] -= 1
            i += 1
        return result
