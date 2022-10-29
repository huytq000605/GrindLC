class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        a = [(plantTime[i], growTime[i]) for i in range(n)]
        a.sort(key = lambda e: (-e[1], e[0]))
        result = 0
        time = 0
        for p, g in a:
            time += p
            result = max(result, time + g)
        return result
