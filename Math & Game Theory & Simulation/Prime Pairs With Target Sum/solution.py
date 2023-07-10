class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [1 for _ in range(n+1)]
        is_prime[0] = 0
        is_prime[1] = 0
        primes = []
        for num in range(2, n+1):
            if is_prime[num]:
                primes.append(num)
                cur = num * num   
            while cur <= n:
                is_prime[cur] = 0
                cur += num
        result = []
        for x in primes:
            if n - x < x:
                break
            if is_prime[x] and is_prime[n-x]:
                result.append([x, n-x])
        return result
