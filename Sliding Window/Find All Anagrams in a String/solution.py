class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        count = [0 for _ in range(26)]
        for c in p:
            count[ord(c) - ord('a')] += 1
        
        def is_anagram():
            for freq in count:
                if freq != 0: return False
            return True
        
        result = []
        for i, c in enumerate(s):
            if i >= m:
                count[ord(s[i-m]) - ord('a')] += 1
            count[ord(c) - ord('a')] -= 1
            if is_anagram():
                result.append(i - m + 1)
        return result
