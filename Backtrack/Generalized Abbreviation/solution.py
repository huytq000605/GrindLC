class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        def gen(i, cur):
            if i == len(word):
                result.append(cur)
                return
            if cur and cur[-1].isdigit():
                gen(i+1, cur + word[i])
                return
            gen(i+1, cur + word[i])
            l = 0
            while i < len(word):
                i += 1
                l += 1
                gen(i, cur + str(l))
        gen(0, "")
        return result
    
