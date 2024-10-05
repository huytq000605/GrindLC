class Solution:
    def clearStars(self, s: str) -> str:
        indexs = [deque() for _ in range(26)]
        for i, c in enumerate(s):
            if c == "*":
                for i in range(26):
                    if indexs[i]: 
                        indexs[i].pop()
                        break
            else:
                indexs[ord(c) - ord('a')].append(i)

        result = ""
        for i, c in enumerate(s):
            if c == "*": continue
            ch = ord(c) - ord('a')
            if (len(indexs[ch]) == 0 or indexs[ch][0] != i): continue
            indexs[ch].popleft()
            result += c
        return result
