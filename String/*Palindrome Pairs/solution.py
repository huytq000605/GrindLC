class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wordDict = dict()
        result = []
        for i in range(len(words)):
            wordDict[words[i]] = i 
        
        def isPalindrome(word):
            left = 0
            right = len(word) - 1
            while left < right:
                if word[left] != word[right]: return False
                left += 1
                right -= 1
            return True
        
        for i in range(len(words)):
            word = words[i]
            for cut in range(1, len(word) + 1):
                first = word[0:cut]
                second = word[cut:]
                if isPalindrome(second):
                    reverseFirst = first[::-1]
                    if reverseFirst in wordDict and wordDict[reverseFirst] != i:
                        result.append([i, wordDict[reverseFirst]])
                
                if isPalindrome(first):
                    reverseSecond = second[::-1]
                    if reverseSecond in wordDict and wordDict[reverseSecond] != i:
                        result.append([wordDict[reverseSecond], i])
                        if reverseSecond == "":
                            result.append([i, wordDict[reverseSecond]])
        
        return result