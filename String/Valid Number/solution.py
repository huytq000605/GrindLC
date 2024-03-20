class Solution:
    def isNumber(self, s: str) -> bool:
        def is_decimal(s):
            if not s: return False
            if s[0] in "+-":
                s = s[1:]
            parts = s.split(".")
            if len(parts) >= 3:
                return False
            has_digit = False
            for part in parts:
                for c in part:
                    if not c.isdigit(): return False
                    has_digit = True
            return has_digit
        
        def is_integer(s):
            if not s: return False
            if s[0] in "+-":
                s = s[1:]
            has_digit = False
            for c in s:
                if not c.isdigit(): return False
                has_digit = True
            return has_digit
        
        count_e = 0
        lower = True
        for c in s:
            if c in "eE":
                count_e += 1
                if count_e > 1: return False
            if c == "E": lower = False
        
        parts = s.split("e" if lower else "E")
        if len(parts) == 1:
            return is_integer(parts[0]) or is_decimal(parts[0])
        return (is_integer(parts[0]) or is_decimal(parts[0])) and is_integer(parts[1])
