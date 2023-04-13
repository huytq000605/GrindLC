class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        n = len(pushed)
        stack = []
        while j < n:
            if stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
            elif i < n:
                stack.append(pushed[i])
                i += 1
            else:
                return False
        return True
