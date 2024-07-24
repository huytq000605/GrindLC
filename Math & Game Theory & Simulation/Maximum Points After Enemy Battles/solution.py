class Solution:
    def maximumPoints(self, es: List[int], e: int) -> int:
        es.sort()
        if e < es[0]:
            return 0
        e += sum(es[1:])
        result = e // es[0]
        return result
            
                
