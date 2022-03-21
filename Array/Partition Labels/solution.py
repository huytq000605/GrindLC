class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = dict()
        for i, l in enumerate(s):
            last_idx[l] = i
        result = []
        i = 0
        while i < len(s):
            l = s[i]
            last = last_idx[l]
            j = i
            while j <= last:
                last = max(last, last_idx[s[j]])
                j += 1
            result.append(j - i)
            i = j
        return result