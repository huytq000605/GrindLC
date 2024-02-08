class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = 0
        n = len(s)
        ones = 0
        result = ""
        for j in range(n):
            if s[j] == "1":
                ones += 1
            
            while ones >= k:
                if ones == k and s[i] == "1":
                    break
                if s[i] == "1": ones -= 1
                i += 1
            
            if ones == k:
                if result == "" or \
                    j-i+1 < len(result) or \
                    (j-i+1 == len(result) and s[i:j+1] < result):
                        result = s[i:j+1]
        return result
