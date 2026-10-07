class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = set()
        def to_remove(s: str) -> bool:
            stack = 0
            result = 0
            for c in s:
                if c == '(': stack += 1
                elif c == ')':
                    stack -= 1
                    if stack < 0:
                        stack = 0
                        result += 1
            return result + stack

        target = to_remove(s)
        if target == 0: return [s]
        q = set([s])
        removed = 0
        while removed < target:
            nq = set()
            end = False
            for s in q:
                for i in range(len(s)):
                    if s[i] in "()":
                        ns = s[:i] + s[i+1:]
                        if removed + 1 + to_remove(ns) == target:
                            nq.add(ns)
            removed += 1
            q = nq
        return list(q)
