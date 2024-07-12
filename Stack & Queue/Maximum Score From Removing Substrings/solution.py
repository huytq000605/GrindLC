class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(s, r, points):
            stack = []
            p = 0
            for c in s:
                stack.append(c)
                while len(stack) >= 2 and stack[-1] == r[-1]\
                    and stack[-2] == r[-2]:
                    stack.pop()
                    stack.pop()
                    p += points
            return stack, p
        
        u, v = "ab", "ba"
        if x < y:
            u, v = v, u
            x, y = y, x
        s, p1 = remove(s, u, x)
        _, p2 = remove(s, v, y)
        return p1 + p2
