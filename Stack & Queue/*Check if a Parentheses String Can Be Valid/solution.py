class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(locked)
        if n % 2 == 1:
            return False
        def validate(s, locked, open_symbol):
            stack = 0
            not_lock = 0
            for i in range(n):
                if locked[i] == "1":
                    if s[i] == open_symbol:
                        stack += 1
                    else:
                        stack -= 1
                else:
                    not_lock += 1
                if stack + not_lock < 0:
                    return False
            return True
        
        return validate(s, locked, "(") and validate(s[::-1], locked[::-1], ")")
