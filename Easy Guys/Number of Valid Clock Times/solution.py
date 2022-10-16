class Solution:
    def countTime(self, time: str) -> int:
        hour = time[:2]
        minute = time[3:]
        result = 1
        if hour[0] == "?" and hour[1] == "?":
            result = 24
        else:
            if hour[0] == "?":
                if int(hour[1]) >= 4:
                    result = 2
                else:
                    result = 3
        
            if hour[1] == "?":
                if hour[0] == "2":
                    result *= 4
                else:
                    result *= 10
        
        if minute[0] == "?":
            result *= 6
        
        if minute[1] == "?":
            result *= 10
        return result
