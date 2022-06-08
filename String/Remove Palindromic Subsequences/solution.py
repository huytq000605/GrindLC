class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        is_palindrome = True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                is_palindrome = False
                break
            i += 1
            j -= 1
        if is_palindrome:
            return 1
        # Delete all a in 1 turn
        # Delete all b in next turn
        return 2