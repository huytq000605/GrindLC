class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = [len(s) for i in range(26)]
        last = [-1 for i in range(26)]
        intervals = []
        
        for i, l in enumerate(s):
            c = ord(l) - ord('a')
            first[c] = min(first[c], i)
            last[c] = max(last[c], i)
        
        for i in range(26):
            if last[i] == -1:
                continue
            original_left = first[i]
            left, right = first[i], last[i]
            j = left
            while j < right and left == original_left:
                l = s[j]
                c = ord(l) - ord('a')
                left = min(left, first[c])
                right = max(right, last[c])
                j += 1
            
            if left == original_left:
                intervals.append((left, right))
                
        intervals.sort(key = lambda interval: interval[1])
        
        prev = -1
        result = []
        for start, end in intervals:
            if start > prev:
                result.append(s[start: end + 1])
            prev = end
        
        return result
          