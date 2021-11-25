class Solution:
    def compress(self, chars: List[str]) -> int:
        currentLetter = chars[0]
        currentFreq = 0
        idx = 0
        result = 0
        for l in chars:
            if l != currentLetter:
                chars[idx] = currentLetter
                idx += 1
                result += 1
                if currentFreq > 1:
                    digits = str(currentFreq)
                    for d in digits:
                        chars[idx] = d
                        idx += 1
                        result += 1
                currentLetter = l
                currentFreq = 1
            else:
                currentFreq += 1
        
        chars[idx] = currentLetter
        idx += 1
        result += 1
        if currentFreq > 1:
            digits = str(currentFreq)
            for d in digits:
                chars[idx] = d
                idx += 1
                result += 1
            
        return result