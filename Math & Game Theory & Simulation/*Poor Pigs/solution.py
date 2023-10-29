class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        times = minutesToTest // minutesToDie
        # Each pig can die at 1 <= t <= times or doesn't die
        # => Each pig can has t+1 states
        # E.g: 
        # pig dies after 1st time
        # pig dies after 2nd time
        # ...
        # pig dies after n-th time
        # pig not die after n-th
        # Strategy to find:
        # In a t time, imagine in a t dimensional
        # Fist pig will test all buckets under have bit at 
        #
        # => (t+1) ^ pigs >= buckets will answer
        pigs = 0
        while (times + 1) ** pigs < buckets:
            pigs += 1
        return pigs
