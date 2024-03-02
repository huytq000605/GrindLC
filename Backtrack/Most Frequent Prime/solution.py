MAX_NUM = 999999
is_prime = [1 for _ in range(MAX_NUM + 1)]
is_prime[0] = 0
is_prime[1] = 0
for num in range(2, MAX_NUM + 1):
    if not is_prime[num]: continue
    cur = num + num
    while cur <= MAX_NUM:
        is_prime[cur] = 0
        cur += num

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        counter = Counter()
        max_freq = 0
        result = -1
        for start_r in range(m):
            for start_c in range(n):
                for dr, dc in ds:
                    num = 0
                    r, c = start_r, start_c
                    while 0 <= r < m and 0 <= c < n:
                        num = num * 10 + mat[r][c]
                        r += dr
                        c += dc
                        if num > 10 and is_prime[num]:
                            counter[num] += 1
                            if counter[num] > max_freq:
                                max_freq = counter[num]
                                result = num
                            elif counter[num] == max_freq:
                                result = max(result, num)
        return result
        
