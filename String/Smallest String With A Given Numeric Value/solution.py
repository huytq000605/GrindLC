class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a' for i in range(n)]
        k -= n
        i = n - 1
        change_to_char = ord('a')
        while k > 0:
            change = min(25, k)
            char = chr(change + change_to_char)
            k -= change
            result[i] = char
            i -= 1
        
        return "".join(result)