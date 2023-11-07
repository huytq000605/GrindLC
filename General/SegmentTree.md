Have both array implementation and tree implementation in DS & Algo
Build Tree takes O(nlogn)
Used for range query efficently in O(logn)
Can stored many values in property to solve problem

Template:
MOD = 10**9 + 7

class SegmentTree:
    def __init__(self, n):
        self.sum = [0 for _ in range(4*n)]
        self.sum_sq = [0 for _ in range(4*n)]
        self.lazy = [0 for _ in range(4*n)]
        self.n = n

    def __update_lazy(self, left, right, i):
        if left != right:
            self.lazy[i*2+1] += self.lazy[i]
            self.lazy[i*2+2] += self.lazy[i]
        gap = right - left + 1
        # 1. (a+1)**2 = a**2 + 2*a + 1
        # considering gap = 2
        # 2. (a+1)**2 + (b+1)**2 = a**2+ b**2 + 2*(a+b) + 2
        # 3. (a+x)**2 + (b+x)**2 = a**2 + b**2 + 2*x*(a + b) + 2 * x**2
        new_sum = self.sum[i] + self.lazy[i] * gap
        new_sum_sq = self.sum_sq[i] + 2 * self.lazy[i] * self.sum[i] + (self.lazy[i]**2) * gap
        self.sum[i] = new_sum % MOD
        self.sum_sq[i] = new_sum_sq % MOD
        self.lazy[i] = 0
    
    
    def add(self, start, end, val, left = 0, right = -1, i = 0):
        if right == -1: right = self.n - 1
        if self.lazy[i]:
            self.__update_lazy(left, right, i)

        if start > right or end < left:
            return
        
        if start <= left and end >= right:
            self.lazy[i] += val
            self.__update_lazy(left, right, i)
            return

        mid = left + (right - left) // 2
        self.add(start, end, val, left, mid, i*2+1)
        self.add(start, end, val, mid + 1, right, i*2+2)
        
        self.sum[i] = (self.sum[i*2+1] + self.sum[i*2+2]) % MOD
        self.sum_sq[i] = (self.sum_sq[i*2+1] + self.sum_sq[i*2+2]) % MOD
        
