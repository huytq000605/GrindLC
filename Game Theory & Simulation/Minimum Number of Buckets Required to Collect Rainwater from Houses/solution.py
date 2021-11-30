class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        result = 0
        for i in range(n):
            if street[i] == "H":
                if (i == 0 or street[i - 1] == "H") and (i == n - 1 or street[i + 1] == "H"):
                    return -1
        
        i = 0
        while i < n:
            if street[i] == "H":
                if i + 1 < n and street[i + 1] == ".":
                    result += 1
                    i += 2
                else:
                    result += 1
            i += 1
        return result
            