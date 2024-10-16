from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = [(-a, "a"), (-b, "b"), (-c, "c")]
        result = ""
        max_heap = []
        for each in freq:
            heappush(max_heap, each)
        while True:
            remaining1, letter1 = heappop(max_heap)
            if len(result) >= 2 and result[-1] == letter1 and result[-2] == letter1:
                remaining2, letter2 = heappop(max_heap)
                if remaining2 != 0:
                    result += letter2
                else:
                    break
                heappush(max_heap, (remaining2+1, letter2))
                heappush(max_heap, (remaining1, letter1))
            elif remaining1 != 0:
                result += letter1
                heappush(max_heap, (remaining1+1, letter1))
            else:
                break
        return result
        
    
        
