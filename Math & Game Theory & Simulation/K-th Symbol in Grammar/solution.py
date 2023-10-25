class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 01
        # 0110
        # 01101001
        if n == 1:
            return 0
        if n == 2 and k == 2:
            return 1
        total = 2 ** (n-1)
        if k <= total // 2:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - (total // 2))
        
