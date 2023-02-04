class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0 for i in range(26)]
        for c in s1:
            count[ord(c) - ord('a')] += 1

        def is_permutation(count):
            for freq in count:
                if freq != 0:
                    return False
            return True

        m = len(s1)
        for i, c in enumerate(s2):
            if i >= m:
                count[ord(s2[i - m]) - ord('a')] += 1
            count[ord(c) - ord('a')] -= 1
            if is_permutation(count):
                return True  
        return False
                
