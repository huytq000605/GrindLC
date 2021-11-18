class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wordDict = {}
        for i in range(len(words)):
            wordDict[words[i]] = i 
        result = []
        
        def isPalindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        
        for i in range(len(words)):
            word = words[i]
            for j in range(0, len(word)):
                
                first = word[:j]
                second = word[j:]
                

                if isPalindrome(first):
                    revSecond = str(second[::-1])
                    if revSecond in wordDict and wordDict[revSecond] != i:
                        result.append([wordDict[revSecond], i])
                
                if isPalindrome(second):
                    revFirst = str(first[::-1])
                    if revFirst in wordDict and wordDict[revFirst] != i:
                        result.append([i, wordDict[revFirst]])
                        if revFirst == "": # Case ["a", ""]
                            result.append([wordDict[revFirst], i])
                        
                        
        return result