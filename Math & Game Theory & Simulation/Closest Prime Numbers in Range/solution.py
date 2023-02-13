class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prev = 0
        diff = math.inf
        result = [-1, -1]
        
        is_prime = [1 if i > 1 else 0 for i in range(right + 1)]
        def sieve():
            for num in range(2, right + 1):
                if is_prime[num]:
                    cur = num * num # num * (factor < num) is already computed
                    while cur <= right:
                        is_prime[cur] = 0
                        cur += num
        sieve()
        for num in range(left, right + 1):
            if is_prime[num]:
                if prev != 0 and num - prev < diff:
                    diff = num - prev
                    result = [prev, num]
                prev = num
        return result
