class Solution:
    def oddString(self, words: List[str]) -> str:
        def diff_arr(word):
            n = len(word)
            diff = []
            for i in range(n-1):
                diff.append(ord(word[i+1]) - ord(word[i]))
            return diff
        
        def eq(a1, a2):
            n = len(a1)
            for i in range(n):
                if a1[i] != a2[i]:
                    return False
            return True
        
        n = len(words)
        diff1, diff2, diff3 = diff_arr(words[0]), diff_arr(words[1]), diff_arr(words[2])
        
        if eq(diff1, diff2):
            for i in range(2, n):
                if not eq(diff_arr(words[i]), diff1):
                    return words[i]
        else:
            if eq(diff1, diff3):
                return words[1]
            else:
                return words[0]
        
