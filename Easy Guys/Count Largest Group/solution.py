class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = [0 for _ in range(37)]
        mx = 0
        for i in range(1, n+1):
            s = 0
            while i:
                s += i % 10
                i //= 10
            groups[s] += 1
            mx = max(mx, groups[s])
        return sum([1 if groups[i] == mx else 0 for i in range(37)]) 
