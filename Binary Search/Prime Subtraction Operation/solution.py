class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        is_prime = [True for _ in range(1001)]
        for num in range(2, 1001):
            if is_prime[num]:
                i = num * num
                while i < 1001:
                    is_prime[i] = False
                    i += num
        primes = [0]
        for num in range(2, 1001):
            if is_prime[num]: primes.append(num)
        n = len(nums)
        m = len(primes)
        for i in range(n):
            if i > 0 and nums[i] <= nums[i-1]:
                return False
            start = 0
            end = m - 1
            while start < end:
                mid = start + math.ceil((end - start + 1) / 2)
                if (i > 0 and nums[i] - primes[mid] <= nums[i-1]) or nums[i] <= primes[mid]:
                    end = mid - 1
                else:
                    start = mid
            nums[i] -= primes[start]
        return True
