class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        def rotatable(i, j):
            down = -1
            for i in range(i+1, j+1):
                if nums[i] < nums[i-1]:
                    if down != -1: return 0
                    down = i
            return down

        snums = sorted(nums)
        n = len(nums)
        result = 0
        ks = []
        k = 1
        while k * k <= n:
            if n % k: 
                k += 1
                continue
            ks.append(k)
            if n // k != k: ks.append(n // k)
            k += 1
            
        for k in ks:
            valid = True
            for i in range(0, n, k):
                r = rotatable(i, i+k-1)
                if not r:
                    valid = False
                    break
                shift = 0 if r == -1 else k - r
                for j in range(k):
                    if nums[i + ((j - shift + k) % k)] != snums[i + j]:
                        valid = False
                        break
            if valid: result += k
        return result
         
