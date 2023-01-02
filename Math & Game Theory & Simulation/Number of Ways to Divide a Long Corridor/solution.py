class Solution:
    def numberOfWays(self, corridor: str) -> int:
        result = 1
        seats = 0
        plants = 0
        for c in corridor:
            if c == "S":
                if seats == 2:
                    seats = 1
                    result *= (plants + 1)
                    plants = 0
                else:
                    seats += 1
            else:
                if seats == 2:
                    plants += 1
        if seats != 2:
            return 0
        return result % (10**9+7)