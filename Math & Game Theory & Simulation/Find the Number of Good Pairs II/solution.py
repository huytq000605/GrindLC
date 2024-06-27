class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        @cache
        def factorial(num):
            result = []
            i = 1
            while i * i <= num:
                if num % i == 0:
                    result.append(num // i)
                    if num // i != i:
                        result.append(i)
                i += 1
            return result
    
        counter = Counter()
        for num in nums1:
            if num % k: continue
            factorials = factorial(num // k)
            for f in factorials: counter[f] += 1
        
        result = 0
        for num in nums2:
            result += counter.get(num, 0)
        return result
