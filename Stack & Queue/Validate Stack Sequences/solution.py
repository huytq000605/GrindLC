class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stack = []
        while j < len(popped):
            while i < len(pushed) and (len(stack) == 0 or popped[j] != stack[-1]):
                stack.append(pushed[i])
                i += 1
            if stack[-1] != popped[j]:
                return False
            stack.pop()
            j += 1
        return True