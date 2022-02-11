class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        letter_s1 = [0 for i in range(26)]
        for l in s1:
            letter_s1[ord(l) - ord('a')] += 1
        
        def compare(arr1, arr2):
            for i in range(26):
                if arr1[i] != arr2[i]:
                    return False
            return True
        
        letter_s2 = [0 for i in range(26)]
        for idx, l in enumerate(s2):
            if idx >= k:
                letter_s2[ord(s2[idx - k]) - ord('a')] -= 1
            letter_s2[ord(l) - ord('a')] += 1
            if idx >= k - 1 and compare(letter_s1, letter_s2):
                return True
        return False
