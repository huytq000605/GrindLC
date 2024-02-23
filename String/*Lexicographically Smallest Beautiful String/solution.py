class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        s = list(map(ord, list(s)))
        # It does not contain any substring of length 2 or more which is a palindrome.
        # -> This means we need to guarantee s[i] != s[i+j] for j in [-2, -1]
        for i in reversed(range(n)):
            # Try to increase each character from right to left
            for ncode in range(s[i] + 1, ord('a') + k):
                valid = True
                for j in range(-2, 0):
                    if i + j < 0:
                        continue
                    if s[i+j] == ncode:
                        valid = False
                # If we can increase this, just fix all the characters from i+1 to end
                if valid:
                    s[i] = ncode
                    # Set all the next characters to either 'a', 'b', 'c' depends on the previous 2 character
                    for i in range(i+1, n):
                        for c in range(3):
                            valid = True
                            for j in range(-2, 0):
                                if i + j < 0:
                                    continue
                                if ord('a') + c == s[i+j]:
                                    valid = False
                                    break
                            if valid:
                                s[i] = ord('a') + c
                                break
                    return "".join(map(chr, s))
                
            
                
        return ""
                 
                
        
