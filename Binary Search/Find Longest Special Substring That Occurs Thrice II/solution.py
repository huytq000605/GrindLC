class Solution:
    def maximumLength(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 0])
            stack[-1][1] += 1
        
        def valid(length):
            freq = Counter()
            for c, l in stack:
                freq[c] += max(0, l - length + 1)
            return max(freq.values()) >= 3
                
        start = 0
        end = len(s)
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if valid(mid):
                start = mid
            else:
                end = mid - 1
        if start == 0: return -1
        return start
