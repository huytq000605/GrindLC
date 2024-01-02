class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        offset = ord('a')
        
        result = 0
        # length can be k, k*1, k*2,.. k*26
        for chars in range(1, 26+1):
            length = chars * k
            if length > len(word): break
            counter = [0 for _ in range(26)]
            # start idx must >= start
            start = 0
            prev = -1
            valid = 0
            for i in range(n):
                if i >= length:
                    c = ord(word[i-length]) - offset
                    if counter[c] == k:
                        valid -= 1
                    counter[c] -= 1
                    
                c = ord(word[i]) - offset
                if prev != -1 and abs(prev - c) > 2:
                    start = i
                
                prev = c
                counter[c] += 1
                if counter[c] == k:
                    valid += 1
                if i - length + 1 >= start and valid == chars:
                    result += 1
        return result

                
            
