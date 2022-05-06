class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for l in s:
            if stack and stack[-1][0] == l:
                stack[-1][1] += 1
            else:
                stack.append([l, 1])
            if stack[-1][1] == k:
                stack.pop()
        result = ""
        for l, freq in stack:
            result += l * freq
        return result