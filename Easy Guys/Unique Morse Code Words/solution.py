class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        count = Counter()
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            morse = ""
            for c in word:
                morse += morses[ord(c) - ord('a')]
            count[morse] += 1
        return len(count.keys())
