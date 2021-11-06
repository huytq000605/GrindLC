class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = 32 * [0]
        def addNum(num):
            for i in range(32):
                arr[i] += (num >> i) & 1 
        
        for num in nums:
            addNum(num)
        result = 0
        negative = False
        for i in range(len(arr)):
            if arr[i] % 3 != 0:
                result = result | (1 << i)
                if i == 31:
                    negative = True
        if negative:
            result = -(2 ** 32 - result)
        
        return result