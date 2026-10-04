class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = []
        stars = []
        for i, c in enumerate(s):
            if c == '(':
                opens.append(i)
            elif c == ')':
                if opens:
                    opens.pop()
                else:
                    if not stars: return False
                    stars.pop()
            else:
                stars.append(i)
        while opens and stars:
            if opens[-1] > stars[-1]: return False
            opens.pop()
            stars.pop() 
        return len(opens) == 0 
                
