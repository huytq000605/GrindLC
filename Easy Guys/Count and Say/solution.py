class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        count = 0
        cur = ""
        result = ""
        for c in self.countAndSay(n-1):
            if c != cur:
                if count > 0:
                    result += str(count) + cur
                count = 0
                cur = c
            count += 1
        result += str(count) + cur
        return result
