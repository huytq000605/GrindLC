class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        powers = [0 for i in range(n)]
        power = sum(stations[:r])
        for i in range(n):
            if i + r < n:
                power += stations[i+r]
            if i - r > 0:
                power -= stations[i-r-1]
            powers[i] = power

        def possible(target):
            put = deque()
            sum_put = 0
            use = 0
            for i, power in enumerate(powers):
                if put and i > put[0][0]:
                    sum_put -= put.popleft()[1]
                power += sum_put
                if power < target:
                    diff = target - power
                    use += diff
                    put.append((i+r+r, diff))
                    sum_put += diff
            if use > k:
                return False
            return True
                    
        start = 0
        end = sum(stations) + k
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if possible(mid):
                start = mid
            else:
                end = mid - 1
        return start
