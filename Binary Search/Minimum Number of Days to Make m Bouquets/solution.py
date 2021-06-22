from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k*m > len(bloomDay): return -1
        minimum = min(bloomDay)
        maximum = max(bloomDay) + 1
        while minimum < maximum:
            middle = minimum + int((maximum - minimum)/2)
            count = 0
            bouquets = 0
            for day in bloomDay:
                if day <= middle:
                    count+=1
                    if count == k:
                        bouquets+=1
                        count = 0
                if day > middle:
                    count = 0
            
            if bouquets < m:
                minimum = middle + 1
            else:
                maximum = middle
        return minimum