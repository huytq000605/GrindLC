class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        deque = collections.deque()
        result = -math.inf
        
        for x,y in points:
            while deque and x - deque[0][0] > k:
                deque.popleft()
                
            if deque:
                result = max(result, y + deque[0][1] + abs(x - deque[0][0]))
                
            while deque and deque[-1][1] - deque[-1][0] <= y - x:
                deque.pop()
            deque.append((x,y))
                
        return result