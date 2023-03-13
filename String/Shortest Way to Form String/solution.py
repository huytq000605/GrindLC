class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        idxs = [[] for _ in range(26)]
        for i, c in enumerate(source):
            idxs[ord(c) - ord('a')].append(i)
        idx = 0
        result = 0
        for c in target:
            c = ord(c) - ord('a')
            if len(idxs[c]) == 0: return -1
            if idx > idxs[c][-1]:
                result += 1
                idx = 0
            start = 0
            end = len(idxs[c]) - 1
            while start < end:
                mid = start + (end - start) // 2
                if idxs[c][mid] >= idx:
                    end = mid
                else:
                    start = mid + 1
            idx = idxs[c][start] + 1
        return result + 1
                
