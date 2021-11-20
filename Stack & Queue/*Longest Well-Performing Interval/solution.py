class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix = [0] * len(hours)
        for i in range(len(hours)):
            if i > 0:
                prefix[i] = prefix[i-1]
            value = 0
            if hours[i] > 8:
                value = 1
            else:
                value = -1
            prefix[i] += value
        
        stack = []
        for start in range(len(prefix)):
            if len(stack) == 0 or prefix[start] < prefix[stack[-1]]:
                stack.append(start)
                
        result = 0
        for end in range(len(prefix) - 1, -1, -1):
            if(prefix[end] > 0):
                result = max(result, end + 1)
            while len(stack) and prefix[end] - prefix[stack[-1]] > 0:
                result = max(result, end - stack.pop())
        return result