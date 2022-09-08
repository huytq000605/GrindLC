class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # 1 2 3 4 5 6 7 8 9
        # D D I D D I D D
        # We push everything to stack, if meet "I", reverse the stack and push these to result
        n = len(pattern)
        stack = []
        result = ""
        for i in range(1, n+1):
            stack.append(str(i))
            if pattern[i-1] == "I":
                while stack: result += stack.pop()
        stack.append(str(n+1))
        while stack:
            result += stack.pop()
        return result
