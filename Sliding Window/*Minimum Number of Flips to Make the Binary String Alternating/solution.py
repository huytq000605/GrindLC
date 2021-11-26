class Solution:
    def minFlips(self, s: str) -> int:
        # operation have meaning when len(s) is odd 
        # because swap 0,1 from odd to even or from even to add
        n = len(s)
        s = s * 2
        def count(startingValue):
            nonlocal s, n
            result = n
            counter = 0
            start = 0
            for i in range(n):
                if i % 2 == 0 and s[i] != startingValue:
                    counter += 1
                elif i % 2 == 1 and s[i] == startingValue:
                    counter += 1
            result = min(result, counter)
            for i in range(n, len(s)):
                if i % 2 == 0 and s[i] != startingValue:
                    counter += 1
                elif i % 2 == 1 and s[i] == startingValue:
                    counter += 1
                if start % 2 == 0 and s[start] != startingValue:
                    counter -= 1
                elif start % 2 == 1 and s[start] == startingValue:
                    counter -= 1
                start += 1
                result = min(result, counter)
            return result
        return min(count("1"), count("0"))