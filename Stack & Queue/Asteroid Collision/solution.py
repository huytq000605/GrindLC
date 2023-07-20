class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for a in asteroids:
            explode = False
            while a < 0 and result and result[-1] > 0:
                if result[-1] < -a:
                    result.pop()
                elif result[-1] == -a:
                    explode = True
                    result.pop()
                    break
                else:
                    explode = True
                    break
            if not explode: result.append(a)
        return result
            
