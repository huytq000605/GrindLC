class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        ss = [0 for i in range(n)]
        for i, s in enumerate(arr):
            valid = True
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if ss[i] | bit != ss[i] + bit:
                    valid = False
                    break
                ss[i] |= bit
            if not valid:
                ss[i] = 0
                arr[i] = ""
        result = 0
        for take in range(1<<n):
            mask = 0
            length = 0
            valid = True
            for i in range(n):
                if (take >> i) & 1:
                    if mask | ss[i] != mask + ss[i]:
                        valid = False
                        break
                    mask |= ss[i]
                    length += len(arr[i])
            if valid:
                result = max(length, result)
        return result
            
                
