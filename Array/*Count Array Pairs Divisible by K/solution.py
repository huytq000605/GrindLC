class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcds = defaultdict(int)
        result = 0
        
        def find_gcd(a, b):
            if b == 0:
                return a
            if a < b:
                a,b = b,a
            return find_gcd(b, a%b)
        
        for num in nums:
            gcd = find_gcd(num, k)
            for seen_gcd, count in gcds.items():
                if (gcd * seen_gcd) % k == 0:
                    result += count
            gcds[gcd] += 1
        return result