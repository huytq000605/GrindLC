class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        result = 0
        for mask in range(1<<n):
            chars = set()
            valid = True
            for i in range(n):
                if not valid: break
                if (mask >> i) & 1 == 0: continue
                for c in arr[i]:
                    if c in chars:
                        valid = False
                        break
                    chars.add(c)
                if valid: result = max(result, len(chars))
        return result
