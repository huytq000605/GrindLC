class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        times = minutesToTest // minutesToDie
        # Each pig can die at 0 <= t <= times or doesn't die
        # => Each pig has (t+1) states
        # => (t+1) ^ pigs >= buckets will answer
        pigs = 0
        while (times + 1) ** pigs < buckets:
            pigs += 1
        return pigs
