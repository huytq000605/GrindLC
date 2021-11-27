class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        a1 = [0] * 32
        a2 = [0] * 32
        # count bits in each position for each arr1 and arr2
        for num in arr1:
            i = 0
            while num > 0:
                a1[i] += num & 1
                num >>= 1
                i += 1
        for num in arr2:
            i = 0
            while num > 0:
                a2[i] += num & 1
                num >>= 1
                i += 1
        # because each num in arr1 AND with each num in arr2
        # total bit in each position = a1[i] * a2[i]
        a = [a1[i] * a2[i] for i in range(32)]
        result = 0
        
        # we XOR all pairs together
        # bit have odd frequency is stay
        for i in range(32):
            if a[i] % 2 != 0:
                result |= (1<<i)
        return result