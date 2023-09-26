class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = dict()
        for i, c in enumerate(s):
            last_idx[c] = i
        in_result = set()
        stack = []
        for i, c in enumerate(s):
            if c in in_result:
                continue
            while stack and last_idx[stack[-1]] > i and c < stack[-1]:
                in_result.remove(stack.pop())
            in_result.add(c)
            stack.append(c)
        return "".join(stack)
