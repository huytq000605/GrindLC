from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        finalFreq = {}
        
        for word in words2:
            freq = {}
            for l in word:
                if freq.get(l) == None: freq[l] = 0
                freq[l] += 1
            for key, value in freq.items():
                if finalFreq.get(key) == None: finalFreq[key] = value
                else: finalFreq[key] = max(finalFreq[key], value)
        
        result = []
        
        for word in words1:
            freq = dict(finalFreq)
            for l in word:
                if freq.get(l) == None: continue
                if freq.get(l) == 1:
                    freq.pop(l)
                    continue
                if freq.get(l) > 1:
                    freq[l] = freq[l] - 1
            if len(freq) == 0:
                result.append(word)
            
        return result