class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for l in logs:
            if l == "../":
                stack = max(0, stack - 1)
            elif l == "./":
                pass
            else:
                stack += 1
        return stack
