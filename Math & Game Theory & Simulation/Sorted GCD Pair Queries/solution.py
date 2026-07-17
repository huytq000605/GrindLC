
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        divisors = defaultdict(int)
        for num in nums:
            i = 1
            while i * i <= num:
                if num % i == 0:
                    divisors[i] += 1
                    if num // i != i:
                        divisors[num//i] += 1
                i += 1
        
        mx = max(nums)
        gcd_count = [0 for _ in range(mx+1)]
        for gcd in range(mx, 0, -1):
            # total pairs having common divisor = gcd
            pairs = divisors[gcd] * (divisors[gcd]-1) // 2
            # exact[gcd] = total_pairs - exact[2*gcd] - exact[3*gcd] - ...
            mul = 2
            while gcd * mul <= mx:
                pairs -= gcd_count[gcd * mul]
                mul += 1
            gcd_count[gcd] = pairs
        
        prefix = [0 for _ in range(mx + 1)]
        for i in range(mx+1):
            if i: prefix[i] = prefix[i-1]
            prefix[i] += gcd_count[i]
        
        return [bisect.bisect(prefix, q) for q in queries]
