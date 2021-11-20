class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        LTR = [-1 for i in range(n)]
        RTL = [n for i in range(n)]
        prefix = [0 for i in range(n)]
        
        for i in range(n):
            if i > 0: prefix[i] = prefix[i - 1]
            if s[i] == "|":
                LTR[i] = i
            else:
                prefix[i] += 1
                if i > 0:
                    LTR[i] = LTR[i-1]
                    
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                RTL[i] = i
            else:
                if i < n - 1:
                    RTL[i] = RTL[i+1]
        result = [0 for i in range(len(queries))]
        for idx, [left, right] in enumerate(queries):
            start = RTL[left]
            end = LTR[right]
            if start < end:
                if start > 0:
                    result[idx] = prefix[end] - prefix[start - 1]
                else:
                    result[idx] = prefix[end]
        return result
            