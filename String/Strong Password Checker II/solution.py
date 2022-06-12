class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        have_lower = False
        have_upper = False
        have_digit = False
        have_special = False
        n = len(password)
        for i in range(n):
            if i > 0 and password[i] == password[i-1]:
                return False
            if password[i].isupper():
                have_upper = True
            elif password[i].islower():
                have_lower = True
            elif password[i].isdigit():
                have_digit = True
            else:
                have_special = True
        if not (have_lower and have_upper and have_digit and have_special):
            return False
        return True
