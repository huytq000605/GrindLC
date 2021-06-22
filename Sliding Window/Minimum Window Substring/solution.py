class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = {}
        for letter in t:
            if counter.get(letter) == None:
                counter[letter] = 0
            counter[letter] += 1
            
        needSatisfy = len(counter)
        
        numOfSatisfy = 0
        
        startResult = 0
        endResult = len(s)
        
        start = 0
        
        for end, letter in enumerate(s):
            if counter.get(letter) != None:
                counter[letter] -= 1
                if counter[letter] == 0:
                    numOfSatisfy += 1
            
            while numOfSatisfy == needSatisfy:
                if end - start < endResult - startResult:
                    startResult = start
                    endResult = end
                    
                if counter.get(s[start]) != None:
                    if counter[s[start]] == 0:
                        break
                    else:
                        counter[s[start]] += 1
                start += 1
                

        if endResult == len(s):
            return ""
        
        return s[startResult:endResult + 1]