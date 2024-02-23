class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        gcds = defaultdict(int)
        result = 0
        for num in nums:
            next_gcds = defaultdict(int)
            if num % k == 0:
                gcds[num] += 1
                for prev_gcd, count in gcds.items():
                    next_gcds[math.gcd(prev_gcd, num)] += count
                result += next_gcds[k]
            gcds = next_gcds
        return result
