class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        result = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            pos, speed = cars[i]
            if stack and speed > cars[stack[0]][1]:
                while len(stack) > 1:
                    if speed <= cars[stack[-1]][1] or (cars[stack[-1]][0] - pos) / (speed - cars[stack[-1]][1]) >= result[stack[-1]]:
                        stack.pop()
                    else:
                        break
                result[i] = (cars[stack[-1]][0] - pos) / (speed - cars[stack[-1]][1])
                stack.append(i)    
            else:
                stack = [i]
                
        return result